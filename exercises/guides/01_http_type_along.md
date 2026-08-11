# Type-Along 01 — HTTP Concepts (30 min)

**Create a new file:** `exercises/my-work/01_answers.txt`

Type your answers after each question. No code yet — just prove you understand the concepts before you script.

---

## Part 1 — Type the HTTP methods (5 min)

In your file, type a line for each method and what it does:

```
GET =
POST =
PATCH =
PUT =
DELETE =
```

Fill in from memory after skimming `cheatsheets/http-api-basics.md`.

<details>
<summary>Check yourself</summary>

```
GET = retrieve data
POST = create something
PATCH = partially update
PUT = replace entirely
DELETE = remove something
```

</details>

---

## Part 2 — Status codes (5 min)

Add to your file — for each code, type what it means AND what you'd do:

```
200 =
201 =
401 =
404 =
409 =
429 =
500 =
```

<details>
<summary>Check yourself</summary>

```
200 = OK — success, use the response
201 = Created — POST worked
401 = Unauthorized — fix API key/token
404 = Not found — wrong URL or ID
409 = Conflict — duplicate, skip or update
429 = Rate limited — slow down, retry later
500 = Server error — retry later
```

</details>

---

## Part 3 — Read JSON (5 min)

Given this response, type the answers in your file:

```json
{
  "data": [
    {"id": "INC-38192", "severity": "critical", "facility": "Plant 4"}
  ],
  "pagination": {"page": 1, "has_more": false}
}
```

Type:
```
data["data"][0]["id"] returns:
data["pagination"]["has_more"] returns:
Number of incidents in this response:
```

<details>
<summary>Check yourself</summary>

```
INC-38192
False
1
```

</details>

---

## Part 4 — Type a Python request from docs (10 min)

Open `mock-apis/README.md`. Find the GET incidents endpoint.

Create **`exercises/my-work/01_first_request.py`** — type this structure yourself (fill in URL and key from the docs):

```python
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SOURCE_API_KEY")
BASE_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")

response = requests.get(
    f"{BASE_URL}/v1/incidents",
    headers={"Authorization": f"Bearer {API_KEY}"},
    params={"status": "open"},
    timeout=30,
)

response.raise_for_status()
data = response.json()

print("Status:", response.status_code)
print("Count:", len(data["data"]))
print("First ID:", data["data"][0]["id"])
```

**Before running:** Start mock APIs in another terminal.

**Run:**
```powershell
python exercises/my-work/01_first_request.py
```

Expected: Status 200, Count 10, First ID something like INC-38192.

If it works, you've done docs → code. That's the skill.

---

## Part 5 — Same request in curl (5 min)

In PowerShell, type this (don't copy from a file — type it):

```powershell
curl -H "Authorization: Bearer dev-source-key-12345" "http://127.0.0.1:5001/v1/incidents?status=open"
```

Add to `01_answers.txt`:
```
The curl -H flag sets:
The ?status=open part is called:
```

<details>
<summary>Check yourself</summary>

```
The curl -H flag sets: a request header
The ?status=open part is called: a query parameter
```

</details>

---

## Done?

Move to **`guides/02_python_type_along.md`**

You should have:
- [ ] `my-work/01_answers.txt`
- [ ] `my-work/01_first_request.py` (runs successfully)
