# HTTP + API Cheat Sheet

## HTTP Methods

| Method | Purpose | Python |
|--------|---------|--------|
| GET | Retrieve data | `requests.get(url)` |
| POST | Create something | `requests.post(url, json=data)` |
| PUT | Replace entirely | `requests.put(url, json=data)` |
| PATCH | Partial update | `requests.patch(url, json=data)` |
| DELETE | Remove something | `requests.delete(url)` |

## Status Codes (memorize these)

| Code | Meaning | Action |
|------|---------|--------|
| 200 | OK | Success |
| 201 | Created | POST succeeded |
| 204 | No content | Success, empty body |
| 400 | Bad request | Check your payload |
| 401 | Not authenticated | Fix API key/token |
| 403 | Not authorized | Key valid but no permission |
| 404 | Not found | Wrong URL or ID |
| 409 | Conflict | Duplicate (idempotency) |
| 429 | Rate limited | Slow down, retry later |
| 500 | Server error | Their problem, retry |

## Request Anatomy

```
GET /v1/incidents?status=open&limit=100 HTTP/1.1
Host: api.example.com
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json
```

## JSON Navigation (Python)

```python
data = response.json()

# Single object
name = data["customer"]["name"]

# List of objects
for alert in data["alerts"]:
    print(alert["severity"])

# Safe access (won't crash if key missing)
severity = data.get("severity", "unknown")
```

## Authentication Patterns

```python
import os

API_KEY = os.getenv("API_KEY")

# Bearer token (most common)
headers = {"Authorization": f"Bearer {API_KEY}"}

# API key header
headers = {"X-API-Key": API_KEY}

# Query param (less common, avoid if possible)
params = {"api_key": API_KEY}
```

## Query Parameters

```python
params = {"status": "open", "limit": 100}
response = requests.get(url, params=params)
# Becomes: url?status=open&limit=100
```

## Same Request in Three Languages

**Python:**
```python
response = requests.get(url, headers={"Authorization": f"Bearer {token}"})
data = response.json()
```

**Bash/curl:**
```bash
curl -H "Authorization: Bearer $TOKEN" https://api.example.com/customers
```

**JavaScript:**
```javascript
const response = await fetch(url, {
  headers: { Authorization: `Bearer ${token}` }
});
const data = await response.json();
```

Same concepts: method, URL, headers, auth, JSON response.

## Reading API Docs → Code

When docs say:

```
POST /v1/work-orders
Authorization: Bearer token
Body: { "site_id": string, "description": string, "priority": "low"|"medium"|"high" }
```

You write:

```python
response = requests.post(
    "https://api.company.com/v1/work-orders",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "site_id": "DAL-1042",
        "description": "Backup generator temperature warning",
        "priority": "high",
    },
)
response.raise_for_status()
print(response.json())
```

## Docs → Postman → Python Flow

```
API Documentation
       ↓
   Postman (manual test)
       ↓
   Inspect JSON response
       ↓
   Convert to Python requests
       ↓
   Add business logic (filter, transform)
       ↓
   Automate + document
```
