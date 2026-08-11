# Python API Syntax — Only What You Need

## Variables and Types

```python
name = "Acme Energy"      # string
count = 10                # integer
active = True             # boolean

customer = {              # dictionary (key → value)
    "name": "Acme",
    "id": 42,
}
print(customer["name"])   # access by key

customers = ["Acme", "Contoso"]  # list
for c in customers:
    print(c)
```

## Conditions and Functions

```python
if count > 5:
    print("Large")

def create_ticket(description, priority):
    return {"description": description, "priority": priority}
```

## Environment Variables

```python
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env file in project root

API_KEY = os.getenv("SOURCE_API_KEY")
if not API_KEY:
    raise ValueError("SOURCE_API_KEY not set")
```

PowerShell to set without .env:
```powershell
$env:SOURCE_API_KEY="dev-source-key-12345"
python script.py
```

## The Core API Pattern

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

response.raise_for_status()   # raises on 4xx/5xx
incidents = response.json()["data"]

for incident in incidents:
    print(incident["id"], incident["severity"])
```

## POST with JSON Body

```python
payload = {
    "external_id": incident["id"],
    "site": incident["facility"],
    "description": incident["message"],
    "priority": 1,
}

response = requests.post(
    f"{DEST_URL}/v1/tickets",
    headers={"Authorization": f"Bearer {DEST_KEY}"},
    json=payload,
    timeout=30,
)
response.raise_for_status()
print(response.json())
```

## Error Handling

```python
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()
except requests.Timeout:
    print("Request timed out")
except requests.HTTPError as e:
    print(f"HTTP error: {e.response.status_code} — {e}")
except requests.RequestException as e:
    print(f"Request failed: {e}")
```

## Pagination Loop

```python
all_records = []
page = 1

while True:
    response = requests.get(
        url,
        headers=headers,
        params={"page": page, "limit": 3},
        timeout=30,
    )
    response.raise_for_status()
    body = response.json()
    records = body["data"]

    if not records:
        break

    all_records.extend(records)

    if not body["pagination"]["has_more"]:
        break

    page += 1
```

## Field Transformation

```python
def transform_incident(incident):
    priority_map = {
        "critical": 1,
        "high": 2,
        "medium": 3,
        "low": 4,
    }
    return {
        "external_id": incident["id"],
        "site": incident["facility"],
        "description": incident["message"],
        "priority": priority_map[incident["severity"]],
    }
```

## What You Can Skip Today

- Classes, inheritance, decorators
- Async/await
- Generators, comprehensions beyond basics
- Algorithms, data structures courses
- pandas, numpy (unless your API returns CSV)

You need: variables, dicts, lists, loops, if/else, functions, imports, requests.
