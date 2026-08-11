# Critical Incident → Ticket Integration

## Purpose

Retrieves critical and high-severity operational incidents from a utility monitoring API and creates corresponding work orders in a ticketing system. Built for Sales Engineers who need a documented, repeatable integration pattern.

## Architecture

```
Monitoring API (source)          Ticketing API (destination)
     GET /v1/incidents      →         POST /v1/tickets
     Bearer auth                     Bearer auth
            ↓                              ↑
            └──── Python sync script ──────┘
                  filter → transform → POST
```

## Requirements

- Python 3.10+
- Dependencies: `pip install -r requirements.txt`

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SOURCE_API_KEY` | Bearer token for monitoring API |
| `DESTINATION_API_KEY` | Bearer token for ticketing API |
| `SOURCE_API_URL` | Base URL (default: `http://127.0.0.1:5001`) |
| `DESTINATION_API_URL` | Base URL (default: `http://127.0.0.1:5002`) |

Copy `.env.example` to `.env` and fill in values.

## Run

```powershell
# Terminal 1 — start mock APIs (for local demo)
python mock-apis/run_servers.py

# Terminal 2 — run sync
python capstone/sync_incidents.py

# Preview without creating tickets
python capstone/sync_incidents.py --dry-run
```

## Flow

1. Load credentials from environment variables
2. Fetch all open incidents (paginated)
3. Filter to `critical` and `high` severity
4. Transform source schema → destination schema
5. POST each ticket; skip duplicates (409 or local state file)
6. Log results

## Field Mapping

| Source (incident) | Destination (ticket) |
|-------------------|----------------------|
| `id` | `external_id` |
| `facility` | `site` |
| `message` | `description` |
| `severity` | `priority` (1–4) |

## Error Handling

- **HTTP failures** — logged, script continues with next incident
- **401/403** — check API keys in `.env`
- **409 Conflict** — ticket already exists; treated as skip
- **Timeouts** — 30s per request
- **Missing env vars** — script exits immediately with clear message

## Security

Credentials are supplied through environment variables and are not committed to source control. The `.env` file is gitignored.

## Idempotency

- Local `processed_ids.json` tracks synced incident IDs across runs
- Destination API returns 409 if `external_id` already exists
- Re-running the script does not create duplicate tickets

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Connection refused | Start mock APIs: `python mock-apis/run_servers.py` |
| 401 Unauthorized | Verify keys in `.env` match mock-apis/README.md |
| No incidents synced | Check severity filter; only critical/high are synced |
