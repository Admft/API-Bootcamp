# Type-Along 04 — Sync System A → System B (60 min)

**Prerequisites:** Mock APIs running, Guide 03 done

**Create a new empty file:** `exercises/my-work/04_sync.py`

You'll fetch incidents from the monitoring API and create tickets in the ticketing API.

---

## Step 1 — Setup (type the boilerplate)

```python
import os

import requests
from dotenv import load_dotenv

load_dotenv()

SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")
DESTINATION_API_KEY = os.getenv("DESTINATION_API_KEY")
SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")
DESTINATION_API_URL = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002")

SYNC_SEVERITIES = {"critical", "high"}
```

Save. Don't run yet — nothing happens without more code.

---

## Step 2 — Transform function (copy from guide 02, from memory)

Type this yourself — don't open 02_basics.py:

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

Quick test — add temporarily:

```python
test = transform_incident({
    "id": "TEST-1",
    "facility": "Test Plant",
    "message": "Test message",
    "severity": "critical",
})
print(test)
```

**Run.** Should print a dict with `priority: 1`. Delete the test lines before continuing.

---

## Step 3 — fetch_open_incidents function

```python
def fetch_open_incidents():
    response = requests.get(
        f"{SOURCE_API_URL}/v1/incidents",
        headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},
        params={"status": "open"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["data"]
```

Test it — add at bottom:

```python
incidents = fetch_open_incidents()
print(f"Got {len(incidents)} incidents")
```

**Run.** Should print `Got 10 incidents`. Remove test lines.

---

## Step 4 — create_ticket function

```python
def create_ticket(payload):
    response = requests.post(
        f"{DESTINATION_API_URL}/v1/tickets",
        headers={"Authorization": f"Bearer {DESTINATION_API_KEY}"},
        json=payload,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()
```

**What you learned:** POST uses `json=payload` — requests sets Content-Type for you.

---

## Step 5 — The main loop (the whole integration)

```python
def main():
    incidents = fetch_open_incidents()
    created = 0

    for incident in incidents:
        if incident["severity"] not in SYNC_SEVERITIES:
            continue

        ticket = transform_incident(incident)

        try:
            result = create_ticket(ticket)
            print(f"Created {result['id']} for {incident['id']}")
            created += 1
        except requests.HTTPError as e:
            print(f"Failed {incident['id']}: {e}")

    print(f"\nSynced {created} tickets.")
```

---

## Step 6 — Entry point

```python
if __name__ == "__main__":
    main()
```

**Run:**
```powershell
python exercises/my-work/04_sync.py
```

You should see lines like `Created TKT-1001 for INC-38192`.

**Run again.** Some may fail with 409 — that's duplicate prevention. Good.

---

## Step 7 — Handle 409 gracefully

Change the `except` block to:

```python
        except requests.HTTPError as e:
            if e.response.status_code == 409:
                print(f"Skipped {incident['id']} — already exists")
            else:
                print(f"Failed {incident['id']}: {e}")
```

**Run again.** Skipped messages instead of errors? Perfect.

**Verify:**
```powershell
python exercises/verify/verify_04.py
```

---

## What you just built

```
Monitoring API  --GET-->  your script  --POST-->  Ticketing API
              incidents          filter + transform        tickets
```

Say that out loud. That's the job description in one sentence.

Next: **Guide 05** (pagination and error handling).
