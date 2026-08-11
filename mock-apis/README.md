# Mock APIs

Two local REST APIs simulate real-world integration endpoints. No internet or paid accounts required.

## Endpoints

### Source — Monitoring API (port 5001)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check (no auth) |
| GET | `/v1/incidents` | List incidents (paginated) |
| GET | `/v1/incidents/{id}` | Get one incident |

**Auth:** `Authorization: Bearer dev-source-key-12345` or `X-API-Key: dev-source-key-12345`

**Query params for `/v1/incidents`:**
- `status` — `open` or `closed`
- `severity` — `critical`, `high`, `medium`, `low`
- `page` — page number (default 1)
- `limit` — records per page (default 100; use `limit=3` to practice pagination)

### Destination — Ticketing API (port 5002)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check (no auth) |
| GET | `/v1/tickets` | List created tickets |
| POST | `/v1/tickets` | Create a ticket |
| GET | `/v1/tickets/by-external/{id}` | Lookup by source ID |

**Auth:** `Authorization: Bearer dev-dest-key-67890`

**POST body:**
```json
{
  "external_id": "INC-38192",
  "site": "Water Treatment Plant 4",
  "description": "Pump pressure below threshold",
  "priority": 1
}
```

Returns `409 Conflict` if `external_id` already exists (practice idempotency).

## Quick test with curl

```powershell
# Health checks
curl http://127.0.0.1:5001/health
curl http://127.0.0.1:5002/health

# Get open critical incidents
curl -H "Authorization: Bearer dev-source-key-12345" "http://127.0.0.1:5001/v1/incidents?status=open&severity=critical"

# Create a ticket
curl -X POST http://127.0.0.1:5002/v1/tickets `
  -H "Authorization: Bearer dev-dest-key-67890" `
  -H "Content-Type: application/json" `
  -d "{\"external_id\":\"INC-38192\",\"site\":\"Water Treatment Plant 4\",\"description\":\"Pump pressure below threshold\",\"priority\":1}"
```

## Start servers

```powershell
python mock-apis/run_servers.py
```
