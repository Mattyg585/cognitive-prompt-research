## Debug Report: Intermittent Order Failures Due to Database Saturation from Runaway Lambda

### Reproduction
- **Expected**: Orders placed via `order-service` are processed successfully, with `inventory-service` responding at its normal latency (p50 ~40ms, p99 ~200ms).
- **Actual**: Approximately 15% of orders fail with `500 Internal Server Error`. The proximate error is `context deadline exceeded` after 5000ms when `order-service` calls `inventory-service`'s `/v2/reserve` endpoint. Failures are intermittent — retries sometimes succeed.
- **Steps**:
  1. Place an order through `order-service` during the incident window (started ~00:30 UTC).
  2. Observe that some orders complete normally while others hang for 5 seconds and then fail with the timeout error.
  3. The failure is probabilistic: the same user, same order payload, sometimes succeeds on retry. This rules out any deterministic input-dependent bug and points toward a resource contention issue downstream.

### Diagnosis

**Hypothesis 1: order-service code or deployment issue.**
Evidence against: No deployments to `order-service` in 48 hours. The only recent change was a config change 3 days ago increasing the request timeout from 3s to 5s. The error originates from waiting on inventory-service, not from order-service's own processing. The stack trace shows the goroutine blocked in `inventory.(*Client).Reserve` — it's waiting on a downstream call, not crashing internally. Eliminated.

**Hypothesis 2: Network issue between order-service and inventory-service.**
Evidence against: Network connectivity has been verified. DNS resolution is fine. The issue is not connection failure — it's latency. Requests that do complete take much longer than normal but the connection itself succeeds. The p50 of 180ms (vs normal 40ms) means connections are being established; it's the processing that's slow. Eliminated.

**Hypothesis 3: inventory-service code or deployment issue.**
Evidence against: No deployments to `inventory-service`. Restarting 2 of 4 pods had no effect, which strongly indicates the bottleneck is not in inventory-service's application code or pod-level state (leaked goroutines, memory pressure, etc.). If the problem were pod-local, restarting should have helped at least for those pods. The problem is downstream of inventory-service. Eliminated as root cause, though inventory-service is in the causal chain.

**Hypothesis 4: PostgreSQL (RDS) is the bottleneck.**
Evidence for: RDS CPU is at 92% (normal 25%). Active connections are at 185 (normal 40). These are both dramatically elevated. Inventory-service connects to this RDS instance, and its elevated response times (p50 4.5x normal, p99 24x normal) are consistent with database queries being queued or executing slowly due to CPU saturation. The intermittent nature of the failure also fits: when a query happens to land during a brief dip in CPU contention, it completes fast enough; when it doesn't, it exceeds the 5-second timeout. This hypothesis explains the symptoms well. Retained — but what is driving the RDS into saturation?

**Hypothesis 5: The `inventory-sync-lambda` is saturating the shared RDS instance.**
Evidence for: This is the critical thread. The Lambda `inventory-sync-lambda` started at 00:15 UTC. Order failures started around 00:30 UTC — 15 minutes later, consistent with a ramp-up period as the Lambda progresses through its work. The Lambda normally completes in 10 minutes but tonight it is still running after 2+ hours. It connects to the same RDS instance as `inventory-service`. The connection count of 185 (vs normal 40) suggests the Lambda is holding or cycling through many connections. The CPU at 92% is consistent with the Lambda running heavy queries (the warehouse sync likely involves bulk reads and writes to inventory tables) while production traffic tries to compete for the same resources.

The Lambda was added 3 weeks ago by a separate team. It runs nightly. The fact that it "usually completes in 10 minutes" but is stuck tonight suggests something changed in the data volume or query plan — perhaps the warehouse system sent a larger-than-usual dataset, or table statistics have drifted causing the query planner to choose a bad execution plan for a larger dataset. Either way, the Lambda is now holding the database hostage.

The timeline locks in this hypothesis:
- 00:15 — Lambda starts
- 00:30 — Order failures begin (Lambda has built up enough load to start starving production queries)
- 02:47 — On-call paged when error rate crosses threshold (the problem has been growing as the Lambda continues)
- Present — Lambda is still running, RDS is still saturated, orders are still failing

**Why restarting inventory-service pods didn't help**: The pods themselves are fine. They're just waiting on a database that can't serve them fast enough. New pods connect to the same overloaded database.

**Why the timeout increase from 3 days ago is relevant**: The change from 3s to 5s timeout means some requests that would have failed at 3s now succeed at 4.x seconds. This is actually masking the true severity — without that change, the failure rate would be higher than 15%. This is also why `retry_count=0` in the logs: the 5s timeout consumes most of the request budget, leaving no room for retries.

### Root Cause

The `inventory-sync-lambda`, a nightly batch job added 3 weeks ago by the warehouse team, is running far longer than its normal 10-minute window. It is saturating the shared PostgreSQL RDS instance (CPU 92%, connections 185) that `inventory-service` also depends on for real-time order processing. Production queries from `inventory-service` must compete with the Lambda's bulk sync operations for CPU cycles and connection slots, causing response times to spike to 24x their normal p99. When those response times exceed order-service's 5-second timeout, the order fails.

This is a resource isolation failure. A batch workload and a latency-sensitive production workload share a database without any mechanism to prevent the batch job from crowding out production traffic.

### Fix

**Immediate (stop the bleeding):**
1. Kill the runaway `inventory-sync-lambda` execution. This should bring RDS CPU and connection counts back to normal within minutes, restoring order processing.
2. Verify recovery by watching RDS CPU drop below 30% and inventory-service p99 return to ~200ms.

**Short-term (prevent recurrence):**
1. Add a maximum execution time limit to the Lambda (e.g., 20 minutes) so a runaway execution self-terminates before it can cause extended production impact.
2. Configure RDS connection limits for the Lambda's database user so it cannot consume more than a fixed share of available connections (e.g., cap at 20 connections, leaving the majority for production).
3. Add an alert on RDS CPU > 60% sustained for 5 minutes, so the team is paged before order failures begin rather than after.

**Structural (match the fix to the actual problem):**
The root cause is a shared resource without isolation. This needs an architectural fix, not just guardrails:
1. Move the Lambda to a read replica for its sync reads, or to a separate database entirely. Batch sync workloads and real-time transactional workloads should not compete for the same database CPU.
2. If a read replica is insufficient (the Lambda may need writes), schedule it during a genuine low-traffic window and implement connection pooling with priority queuing so production queries are always served first.
3. Establish a cross-team review process for any new workload connecting to production databases. The Lambda was added by the warehouse team without (apparently) coordinating with the team that owns inventory-service and its database. Shared infrastructure needs shared awareness.

### Prevention
- Add an integration test or canary that monitors `inventory-service` p99 latency and alerts at 500ms (2.5x normal), providing early warning before order-level timeouts occur.
- Add a runbook for the `inventory-sync-lambda`: what it does, when it runs, how to kill it, and what symptoms its failure modes produce in downstream services.
- Implement RDS CPU and connection count alerts with thresholds well below the saturation point (e.g., CPU > 50%, connections > 80).
- Tag the Lambda's database connections with a distinct application name so that `pg_stat_activity` queries can immediately distinguish batch load from production load during future incidents.
- Add a circuit breaker or adaptive timeout in `order-service`'s inventory client: if inventory-service is consistently slow, fail fast and return a meaningful error to the user rather than tying up goroutines for 5 seconds each. This won't prevent the root cause but limits blast radius and preserves order-service stability during downstream degradation.
