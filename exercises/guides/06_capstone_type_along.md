# Type-Along 06 — Connected Operations POC (90 min)

**Create a new empty file:** `exercises/my-work/06_sync_incidents.py`

Combine everything: fetch, paginate, filter, transform, POST, handle errors, and log results. Treat the script as a customer proof of concept, not just a coding assignment.

Before coding, read the customer scenario and discovery questions in `ROLE_PLAYBOOK.md`. State the customer problem and POC success criteria out loud.

Don't look at `capstone/sync_incidents.py` until you're done.

---

## Step 1 — Imports and constants

```python
import os

import requests
from dotenv import load_dotenv

load_dotenv()

SYNC_SEVERITIES = {"critical", "high"}
PRIORITY_MAP = {"critical": 1, "high": 2, "medium": 3, "low": 4}
```

---

## Step 2 — load_config function

```python
def load_config():
    source_key = os.getenv("SOURCE_API_KEY")
    dest_key = os.getenv("DESTINATION_API_KEY")
    source_url = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001").rstrip("/")
    dest_url = os.getenv("DESTINATION_API_URL", "http://127.0.0.1:5002").rstrip("/")

    if not source_key or not dest_key:
        raise ValueError("Set SOURCE_API_KEY and DESTINATION_API_KEY in .env")

    return {
        "source_key": source_key,
        "dest_key": dest_key,
        "source_url": source_url,
        "dest_url": dest_url,
    }
```

---

## Step 3 — transform (you've done this twice — type from memory)

```python
def transform_incident(incident):
    return {
        "external_id": incident["id"],
        "site": incident["facility"],
        "description": incident["message"],
        "priority": PRIORITY_MAP[incident["severity"]],
    }
```

---

## Step 4 — fetch with pagination

```python
def fetch_all_open_incidents(config):
    all_incidents = []
    page = 1
    headers = {"Authorization": f"Bearer {config['source_key']}"}

    while True:
        response = requests.get(
            f"{config['source_url']}/v1/incidents",
            headers=headers,
            params={"status": "open", "page": page, "limit": 100},
            timeout=30,
        )
        response.raise_for_status()
        body = response.json()
        records = body["data"]

        if not records:
            break

        all_incidents.extend(records)

        if not body["pagination"]["has_more"]:
            break
        page += 1

    return all_incidents
```

---

## Step 5 — create_ticket

```python
def create_ticket(config, payload):
    response = requests.post(
        f"{config['dest_url']}/v1/tickets",
        headers={"Authorization": f"Bearer {config['dest_key']}"},
        json=payload,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()
```

---

## Step 6 — sync function (the orchestrator)

Type this carefully:

```python
def sync():
    config = load_config()

    print("Fetching incidents...")
    incidents = fetch_all_open_incidents(config)
    print(f"  {len(incidents)} open incidents")

    to_sync = [i for i in incidents if i["severity"] in SYNC_SEVERITIES]
    print(f"  {len(to_sync)} critical/high to sync\n")

    stats = {"created": 0, "skipped": 0, "failed": 0}

    for incident in to_sync:
        ticket = transform_incident(incident)
        try:
            result = create_ticket(config, ticket)
            print(f"  OK  {result['id']} <- {incident['id']}")
            stats["created"] += 1
        except requests.HTTPError as e:
            if e.response.status_code == 409:
                print(f"  SKIP {incident['id']} (duplicate)")
                stats["skipped"] += 1
            else:
                print(f"  FAIL {incident['id']}: {e}")
                stats["failed"] += 1

    print(f"\nDone: {stats['created']} created, {stats['skipped']} skipped, {stats['failed']} failed")
```

---

## Step 7 — Entry point

```python
if __name__ == "__main__":
    sync()
```

**Run:**
```powershell
python exercises/my-work/06_sync_incidents.py
```

**Run again.** More skips, fewer creates? Idempotency working.

---

## Step 8 — Document it like an SE (20 min)

Create `exercises/my-work/06_README.md` — type your own using this outline:

1. **Customer problem and business outcome**
2. **Measurable POC success criteria**
3. **Environment variables** — table
4. **How to run**
5. **Field mapping** — source column → destination column
6. **What happens on errors and duplicates**
7. **Assumptions and production-validation steps**

Compare with `templates/integration-readme-template.md` when done.

---

## Step 9 — Final test

Restart mock APIs (clears tickets), run your script fresh.

Then deliver the five-minute demo in `ROLE_PLAYBOOK.md`. Do not narrate code line by line—explain the workflow, customer value, technical choices, limitations, and next step.

Finally, open `SELF_TEST.md` and try rebuilding a minimal version from **blank file** in under 45 minutes.

You passed the bootcamp when you can build it without guides and explain it clearly to both technical and non-technical stakeholders.
