# Exercise 01 — HTTP + API Concepts (30 min)

Read `cheatsheets/http-api-basics.md` first, then answer these without looking.

## Part A: Match HTTP method to action

| Method | Action |
|--------|--------|
| 1. GET | A. Create a new record |
| 2. POST | B. Retrieve data |
| 3. PATCH | C. Delete a record |
| 4. DELETE | D. Partially update a record |

<details>
<summary>Answers</summary>

1-B, 2-A, 3-D, 4-C

</details>

## Part B: Status codes

What should you do when you see each code?

| Code | Meaning | Your action |
|------|---------|-------------|
| 200 | | |
| 201 | | |
| 401 | | |
| 404 | | |
| 409 | | |
| 429 | | |
| 500 | | |

<details>
<summary>Answers</summary>

| Code | Meaning | Action |
|------|---------|--------|
| 200 | OK | Success — parse response |
| 201 | Created | POST succeeded |
| 401 | Unauthorized | Fix API key / token |
| 404 | Not found | Wrong URL or ID |
| 409 | Conflict | Duplicate — skip or update |
| 429 | Rate limited | Wait and retry |
| 500 | Server error | Retry later |

</details>

## Part C: Read this JSON

```json
{
  "data": [
    {
      "id": "INC-38192",
      "facility": "Water Treatment Plant 4",
      "severity": "critical",
      "message": "Pump pressure below threshold"
    }
  ],
  "pagination": {
    "page": 1,
    "has_more": false
  }
}
```

Without running code, write what each Python expression returns:

1. `data["data"][0]["id"]` → ?
2. `data["pagination"]["has_more"]` → ?
3. How many incidents in this response? → ?

<details>
<summary>Answers</summary>

1. `"INC-38192"`
2. `False`
3. `1`

</details>

## Part D: Docs → Request

Given this API documentation:

```
GET /v1/incidents
Authorization: Bearer {token}
Query: status (optional), page (optional), limit (optional)
```

Write the Python `requests.get()` call (you don't need real values):

<details>
<summary>Answer</summary>

```python
response = requests.get(
    "https://api.example.com/v1/incidents",
    headers={"Authorization": f"Bearer {token}"},
    params={"status": "open", "page": 1, "limit": 100},
    timeout=30,
)
response.raise_for_status()
```

</details>

## Part E: Security

Why is this bad?

```python
API_KEY = "abc123-secret-key"
```

What's the fix?

<details>
<summary>Answer</summary>

The key is hardcoded in source code — it gets committed to git, shared in screenshots, and can't differ per environment.

Fix:
```python
import os
API_KEY = os.getenv("API_KEY")
```

</details>

## Done?

Move to Postman (Exercise 01b below) or open `postman/README.md`.
