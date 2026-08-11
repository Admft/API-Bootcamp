# Type-Along 05 — Pagination & Error Handling (45 min)

**Create a new empty file:** `exercises/my-work/05_reliability.py`

Real APIs don't return everything at once. Real requests fail. You'll handle both.

---

## Step 1 — Boilerplate

```python
import os

import requests
from dotenv import load_dotenv

load_dotenv()

SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")
SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")

HEADERS = {"Authorization": f"Bearer {SOURCE_API_KEY}"}
```

---

## Step 2 — Paginated fetch (type the while loop)

```python
def fetch_all_incidents(limit=3):
    all_records = []
    page = 1

    while True:
        print(f"Fetching page {page}...")
        response = requests.get(
            f"{SOURCE_API_URL}/v1/incidents",
            headers=HEADERS,
            params={"page": page, "limit": limit},
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

    return all_records
```

Test at bottom:

```python
all_incidents = fetch_all_incidents(limit=3)
print(f"Total: {len(all_incidents)} incidents across all pages")
```

**Run it.** You should see multiple "Fetching page..." lines and `Total: 12`.

**Why limit=3?** Forces pagination with our mock data so you practice the loop.

---

## Step 3 — safe_get with try/except

Remove the test lines. Add:

```python
def safe_get_incident(incident_id):
    try:
        response = requests.get(
            f"{SOURCE_API_URL}/v1/incidents/{incident_id}",
            headers=HEADERS,
            timeout=30,
        )
        response.raise_for_status()
        return response.json()

    except requests.Timeout:
        print(f"  Timeout fetching {incident_id}")
        return None

    except requests.HTTPError as e:
        if e.response.status_code == 404:
            print(f"  {incident_id} not found")
        elif e.response.status_code == 401:
            print("  Auth failed — check SOURCE_API_KEY")
        else:
            print(f"  HTTP {e.response.status_code}: {e}")
        return None

    except requests.RequestException as e:
        print(f"  Request failed: {e}")
        return None
```

---

## Step 4 — Test success and failure

```python
if __name__ == "__main__":
    print("=== Pagination ===")
    all_incidents = fetch_all_incidents(limit=3)
    print(f"Total: {len(all_incidents)}\n")

    print("=== Safe GET — exists ===")
    found = safe_get_incident("INC-38192")
    print(f"  Result: {found['id'] if found else None}\n")

    print("=== Safe GET — missing ===")
    missing = safe_get_incident("INC-99999")
    print(f"  Result: {missing}\n")

    print("Exercise 05 complete.")
```

**Run it.**

**Verify:**
```powershell
python exercises/verify/verify_05.py
```

---

## Step 5 — Break it on purpose (learn from errors)

Temporarily set a bad key in your script (don't save this):

```python
HEADERS = {"Authorization": "Bearer wrong-key"}
```

**Run safe_get_incident("INC-38192").** See the 401 message?

Fix the key back. Errors you cause yourself stick better than reading about them.

Next: **Guide 06** — build the full capstone yourself.
