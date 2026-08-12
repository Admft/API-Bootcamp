# Connected Operations Event → Work Order POC

## Purpose

Retrieves critical and high-severity operational events from a connected-operations API and creates corresponding work orders in a customer's ticketing system. It simulates the type of open-API proof of concept a Samsara Sales Engineer may build and document.

The local APIs and schemas are fictional training resources, not official Samsara endpoints.

## Customer Problem

Dispatch and maintenance teams currently copy urgent events into their work-order system by hand. The delay and inconsistent data entry can slow response, create duplicate effort, and weaken reporting.

## POC Success Criteria

- Every open critical or high-severity event becomes a correctly mapped work order
- Running the integration again does not create duplicates
- Credentials do not appear in source code
- Operators can see created, skipped, and failed counts
- Another Sales Engineer can run and explain the POC from the documentation

## Architecture

```
Connected operations API        Customer work-order API
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

## Discovery Assumptions to Validate

- Which event types and severities require action?
- Which team owns each generated work order?
- What response time does the customer need?
- Which destination fields are mandatory?
- Should the production design poll, consume webhooks, or use another event mechanism?
- What volume, rate limits, retention, and security controls apply?

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

## Demo Talk Track

1. Restate the customer's manual workflow and desired outcome
2. Show the authenticated GET and JSON response in Postman
3. Run the Python script and show the created work orders
4. Run it again and explain the duplicate skips
5. Explain the data mapping, errors, security, and deployment assumptions
6. Close with production-validation steps and measurable POC acceptance criteria

See `ROLE_PLAYBOOK.md` for the complete five-minute demo.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Connection refused | Start mock APIs: `python mock-apis/run_servers.py` |
| 401 Unauthorized | Verify keys in `.env` match mock-apis/README.md |
| No incidents synced | Check severity filter; only critical/high are synced |
