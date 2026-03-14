# Test Material: Bug Report

## The Problem

**Reported by**: On-call engineer (paged at 2:47 AM)
**Environment**: Production (AWS, us-east-1)
**Service**: `order-service` (Go, runs on EKS)
**Severity**: Customer-impacting — orders intermittently failing

## What's Happening

Approximately 15% of orders placed in the last 2 hours are failing with a `500 Internal Server Error`. The failures are intermittent — the same user can retry and sometimes succeed. No deployment in the last 48 hours. No infrastructure changes.

## Error Message

```
2026-03-14T02:47:12Z ERROR order-service/handler.go:142 failed to process order
    error="context deadline exceeded"
    order_id="ord_8f3k2m"
    user_id="usr_29dk3"
    duration_ms=5003

2026-03-14T02:47:12Z ERROR order-service/handler.go:156 downstream call failed
    service="inventory-service"
    endpoint="/v2/reserve"
    error="context deadline exceeded"
    timeout_ms=5000
    retry_count=0
```

## Stack Trace

```
goroutine 847 [select]:
order-service/internal/inventory.(*Client).Reserve(0xc000234000, {0x1a2b3c4, 0xc000567890}, {0xc000345678, 0x3})
    /app/internal/inventory/client.go:89 +0x1a4
order-service/internal/handler.(*OrderHandler).CreateOrder(0xc000123000, {0x1a2b3c4, 0xc000567890}, 0xc000789abc)
    /app/internal/handler/handler.go:142 +0x2b8
```

## What We Know

- Started around 00:30 UTC, noticed at 02:47 when error rate crossed the alert threshold
- `inventory-service` response times are elevated: p50 = 180ms (normal: 40ms), p99 = 4800ms (normal: 200ms)
- `inventory-service` had no deployments either
- `inventory-service` connects to PostgreSQL (RDS, db.r6g.xlarge)
- RDS metrics show: CPU at 92% (normal: 25%), active connections at 185 (normal: 40), read IOPS normal
- CloudWatch shows a Lambda function `inventory-sync-lambda` started running at 00:15 UTC — it's a scheduled job that syncs inventory counts from the warehouse system. It's still running.
- The Lambda was added 3 weeks ago by another team. It runs nightly and usually completes in 10 minutes. Tonight it appears to be stuck or running much longer than usual.
- The Lambda connects to the same RDS instance as `inventory-service`

## Recent Changes (Last 7 Days)

- 3 days ago: `order-service` config change — increased request timeout from 3s to 5s (explaining why some requests succeed now that they have more time)
- 3 weeks ago: `inventory-sync-lambda` deployed by warehouse team
- No code deployments to `order-service` or `inventory-service`

## What's Been Tried

- Restarted 2 of 4 `inventory-service` pods — no improvement
- Checked network connectivity between services — fine
- Verified no DNS resolution issues

## The Task

Debug this issue using the `/debug` template from the prompt. Reproduce, isolate, diagnose, and propose a fix.
