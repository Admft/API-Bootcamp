# Request Anatomy (what every API call has)

```
GET /v1/incidents?status=open HTTP/1.1
Host: 127.0.0.1:5001
Authorization: Bearer YOUR_TOKEN
```

| Piece | Meaning |
|-------|---------|
| **Method** | GET |
| **Path / endpoint** | `/v1/incidents` |
| **Query parameter** | `status=open` (after `?`) |
| **Header** | `Authorization: Bearer …` |
| **Body** | Empty for GET; JSON for POST |

## JSON response (you'll parse this in Python)

```json
{
  "data": [
    {"id": "INC-38192", "severity": "critical", "facility": "Plant 4"}
  ],
  "pagination": {"page": 1, "has_more": false}
}
```

In Python:

```python
body = response.json()
first_id = body["data"][0]["id"]          # → "INC-38192"
has_more = body["pagination"]["has_more"] # → False
```

## Auth you'll use today

```python
headers = {"Authorization": f"Bearer {API_KEY}"}
```

Keys live in `.env` — never commit them.

**Next:** baby Python type-alongs. One tiny skill at a time.
