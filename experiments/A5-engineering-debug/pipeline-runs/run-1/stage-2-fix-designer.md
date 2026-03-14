## Fix Proposal: Order Processing Failures from Shared-Database Saturation by Uncontrolled Batch Job

### Immediate Mitigation

The system is actively degraded. The `inventory-sync-lambda` has been running for 2.5+ hours against a shared production database, saturating it at 92% CPU and causing 15% order failures. Two actions to stop the bleeding:

**1. Kill the runaway Lambda execution.**

Invoke the Lambda's stop/cancel mechanism (or terminate it via the AWS console / CLI). The Lambda is not completing its work productively — it's been running 15x longer than normal. Stopping it will release its database connections and CPU-intensive queries, allowing `inventory-service` latency to recover. Before killing it, capture its current state from CloudWatch logs and `pg_stat_activity` for post-incident analysis.

If the Lambda is mid-transaction, killing it will cause PostgreSQL to roll back the transaction. On a heavily loaded RDS instance at 92% CPU, rollback of a large transaction can itself be expensive — monitor RDS CPU and connection counts after the kill to confirm recovery. If the Lambda is running many small transactions, rollback cost will be negligible.

**2. Revert the timeout increase on `order-service` from 5s back to 3s.**

This is counterintuitive — won't a shorter timeout cause *more* failures? Under normal conditions, yes. Under database contention, no. The 5s timeout is actively making the contention worse: every request that hangs for 4.5s before succeeding holds a database connection for 4.5s instead of failing at 3s and releasing it. The longer timeout increases the steady-state connection count against the database, deepening the resource pressure. Reverting to 3s will cause some marginal requests to fail that would have scraped through at 5s, but it will reduce the connection load on the database, improving latency for all other requests. This is the correct tradeoff during contention.

This revert should happen *after* killing the Lambda. If the Lambda kill restores database performance to normal (p99 back under 200ms), the timeout revert becomes less urgent — but it should still happen because the 5s timeout creates latent risk for the next contention event.

**3. Order reconciliation.**

Failed orders during the incident window (00:30 - present) need reconciliation. If the payment service processes charges before inventory reservation, some customers may have been charged without receiving order confirmations. If the system allows retries, some customers may have placed duplicate orders. The reconciliation should cross-reference payment records against confirmed orders for the incident window and resolve discrepancies. This is a business operations task, not an engineering fix, but it needs to be initiated now.

### Structural Fix

**What to change**: Isolate the batch workload from the production read/write path at the database layer.

**At what level**: Architecture and Process. This is not a code bug or a configuration knob — it's a missing architectural boundary. Two workloads with fundamentally different resource profiles (low-latency transactional queries vs. long-running bulk sync operations) share a database with no isolation. The fix needs to separate them.

**The fix has three parts:**

**Part 1 — Database resource isolation for the Lambda.**

Create a read replica for the `inventory-sync-lambda` to use for its read-heavy sync operations. The Lambda's job is to sync inventory counts from the warehouse system, which is primarily reading current state and computing deltas. The reads should go to a replica. The writes (applying the sync results) should go to the primary, but through a controlled path:

- The Lambda should use a dedicated database user/role with connection limits enforced at the PostgreSQL level (`ALTER ROLE sync_lambda CONNECTION LIMIT 5`). This prevents the Lambda from consuming unbounded connections regardless of what happens in its execution.
- The Lambda's write operations should be batched into small, bounded transactions — not one giant transaction that holds locks for hours. Each batch should commit independently. If the Lambda is currently running as a single transaction, this is the most important change.
- The Lambda should use `statement_timeout` on its database role (e.g., `ALTER ROLE sync_lambda SET statement_timeout = '30s'`) so that any individual query that runs longer than 30 seconds is killed rather than allowed to saturate the database indefinitely.

**Part 2 — Circuit breaker between `order-service` and `inventory-service`.**

The current architecture has no mechanism for `order-service` to detect that `inventory-service` is degraded and respond differently. It sends every request and waits for timeout. Under sustained degradation, this means every order attempt consumes resources (connections, threads, timeout duration) before failing.

Add a circuit breaker on `order-service`'s call to `inventory-service /v2/reserve`:
- **Closed** (normal): requests flow through.
- **Open** (tripped): after N failures within a window, stop sending requests and fail immediately with a meaningful error ("inventory service temporarily unavailable, please retry shortly") instead of waiting 5s per request to timeout.
- **Half-open**: periodically allow a probe request through to detect recovery.

This doesn't prevent the underlying problem, but it prevents `order-service` from compounding the damage by piling requests onto a degraded downstream, and it gives customers an immediate failure instead of a 5s hang followed by a failure.

**Part 3 — Timeout strategy.**

The 3s-to-5s timeout change was made without analysis of its system-wide effects. The timeout on `order-service`'s call to `inventory-service` should be set based on the *normal* latency distribution with headroom, not increased reactively when requests start timing out. The correct response to requests timing out at 3s is to investigate why latency increased, not to increase the timeout.

Set the timeout to a value that accommodates the normal p99 (200ms) with reasonable headroom — 1s to 1.5s is appropriate. A request that takes more than 1.5s to reserve inventory is already anomalous and indicates a systemic problem that a longer timeout will not solve. Combined with the circuit breaker, this means degradation is detected and surfaced quickly rather than masked.

**Rationale**: The root cause is not a bug — it's a missing architectural boundary. The Lambda and `inventory-service` are operated by different teams with different operational concerns, yet they share a critical resource (the database) with no isolation. The Lambda team had no visibility into the production impact of their batch job, and the `order-service` team had no mechanism to protect against downstream degradation. The fix creates the boundaries that should have existed before the Lambda was introduced: resource limits at the database layer, workload isolation via a replica, and a circuit breaker to contain blast radius.

### Implementation Considerations

**Side effects**:
- Read replica introduces replication lag. The Lambda reading from a replica will see slightly stale data. For an inventory sync job that runs nightly, this is acceptable — the warehouse data it's syncing is already hours old.
- Connection limits on the Lambda's database role will cause the Lambda to fail if it tries to open more than the allowed connections. The Lambda code must handle this gracefully — retry with backoff, or use a connection pool that respects the limit.
- The circuit breaker will cause `order-service` to fail orders *faster* during degradation. This is the intended behaviour, but it changes the failure mode from "slow failure after timeout" to "fast failure with circuit open." Downstream systems and the customer-facing error handling must be aware of this new failure mode.
- Reducing the timeout from 5s to 1-1.5s will cause requests that currently succeed between 1.5s and 5s to fail. Under normal operation (p99 = 200ms), virtually no requests fall in this range. Under degradation, many do — but those requests succeeding at 4s is itself a symptom of the problem, not a feature to preserve.

**Edge cases**:
- If the Lambda legitimately needs to process a very large dataset (e.g., annual full inventory reconciliation), the connection limit and statement timeout may cause it to fail. The Lambda should be designed to handle this gracefully — chunked processing, progress tracking, resumability. Very large syncs should be scheduled during a maintenance window with advance coordination, not run as an unattended nightly job.
- If the read replica falls significantly behind (minutes of lag), the Lambda's sync calculations based on stale data could produce incorrect deltas. The Lambda should check replication lag before proceeding and abort or alert if lag exceeds a threshold.

**Regression risks**:
- The most likely regression is the Lambda failing on its next run due to the new connection limits or statement timeouts. This is a controlled failure — it's better for the Lambda to fail visibly than to succeed silently while degrading production. The Lambda team needs to be informed and prepared to adapt.
- Reducing `order-service` timeout could cause regressions if there are legitimate slow paths in `inventory-service` that currently depend on the 5s timeout. Review `inventory-service` latency data under normal conditions to confirm that 1-1.5s accommodates the normal distribution.

**Dependencies**:
- **Warehouse/Lambda team**: They own `inventory-sync-lambda` and need to implement connection pooling, transaction batching, and the read-replica migration. This is the most significant coordination requirement.
- **Platform/DBA team**: Creating the read replica, configuring the sync role with connection limits and statement timeouts, and potentially reviewing RDS instance sizing.
- **Order-service team**: Implementing the circuit breaker and reverting/adjusting the timeout.
- **Business operations**: Order reconciliation for the incident window.

### Verification

**How to verify the fix works**:
- After killing the Lambda: RDS CPU should drop from 92% toward the 25% baseline within minutes. Active connections should drop from 185 toward 40. `inventory-service` p99 latency should return to the ~200ms range. `order-service` error rate should drop to zero. If these metrics don't recover after killing the Lambda, the root cause analysis may be incomplete — check for lingering transactions, vacuum pressure, or bloated tables from the Lambda's partial writes.
- After implementing resource isolation: Run the Lambda during business hours (intentionally, in a controlled test) with the connection limits and statement timeouts in place. Verify that `inventory-service` latency is unaffected during the Lambda's execution. Verify that the Lambda completes successfully within its normal runtime using the read replica for reads.
- After implementing the circuit breaker: Simulate `inventory-service` degradation (inject latency in a staging environment) and verify that the circuit breaker trips, that `order-service` returns fast failures, and that the circuit breaker recovers when `inventory-service` latency returns to normal.

**How to verify nothing else broke**:
- Monitor the Lambda's next nightly run end-to-end. Confirm it completes successfully with the new connection limits and read-replica configuration. Compare its output (inventory sync results) against previous successful runs.
- Monitor `order-service` error rates and latency after the timeout reduction to confirm no regression under normal conditions.
- Check whether any other services or jobs connect to this RDS instance and verify they are unaffected by the new role-level connection limits (which apply only to the Lambda's role).

### Prevention

**1. Connection-limit enforcement for all batch/async consumers of production databases.**
- *What it prevents*: Any batch job saturating a shared production database with unbounded connections — the exact failure mode seen tonight.
- *Where*: Enforced at the PostgreSQL role level for every non-application consumer of production databases. Codified in the infrastructure-as-code (Terraform, CloudFormation) that provisions database access for new consumers.
- *Relationship to root cause*: The Lambda was introduced 3 weeks ago with unrestricted database access. If connection limits had been a standard requirement for any new database consumer, this failure class would not exist.

**2. Runtime anomaly alerting on scheduled jobs.**
- *What it catches*: A scheduled job running significantly longer than its historical baseline — exactly what happened tonight with the Lambda running 15x longer than normal without any alert.
- *Where*: CloudWatch alarm on Lambda duration, configured relative to the job's historical p95 runtime. For a job that normally runs 10 minutes, alert at 20 minutes.
- *Relationship to root cause*: The Lambda ran for 2.5+ hours before anyone was paged, and the page was triggered by the *symptom* (`order-service` errors), not the *cause* (Lambda runtime anomaly). An alert on Lambda duration would have surfaced the cause directly, potentially before customer impact.

**3. Shared-resource review in the change management process for new database consumers.**
- *What it prevents*: A team introducing a new workload against a shared production database without understanding or mitigating its impact on existing consumers.
- *Where*: The change management or architecture review process. When a team proposes a new consumer of a production database, the review should assess: What is the query profile? What is the expected connection count? What is the worst-case runtime? Is resource isolation needed? This is not a heavyweight process — it's a checklist.
- *Relationship to root cause*: The Lambda was introduced by the warehouse team without (apparently) any coordination with the team that operates `inventory-service` or the database. A review would have identified the shared-resource risk and required isolation controls before deployment.

**4. Database resource monitoring with consumer-level attribution.**
- *What it catches*: Any single consumer disproportionately consuming database resources, before it degrades other consumers.
- *Where*: RDS Performance Insights or equivalent, with alerting segmented by database user/role. This requires each consumer to use a distinct database role (which the structural fix establishes for the Lambda).
- *Relationship to root cause*: Tonight, the RDS metrics showed aggregate saturation (92% CPU, 185 connections) but did not attribute the load to the Lambda vs. `inventory-service`. With per-role monitoring, the Lambda's resource consumption would have been visible and alertable independently.
