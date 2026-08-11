# Type-Along 03 — Your First API Script (45 min)

**Prerequisites:** Mock APIs running (`python mock-apis/run_servers.py`)

**Create a new empty file:** `exercises/my-work/03_get_incidents.py`

You'll build a script that calls a real API and prints critical incidents.

---

## Step 1 — Imports and config

Type this at the top:

```python
import os

import requests
from dotenv import load_dotenv

load_dotenv()

SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")
SOURCE_API_URL = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")
```

**What you learned:** `load_dotenv()` reads your `.env` file. Secrets never go in code.

---

## Step 2 — Print config (sanity check)

Add:

```python
print("Connecting to:", SOURCE_API_URL)
print("API key loaded:", "yes" if SOURCE_API_KEY else "NO — check .env")
```

**Run it.** Should say `Connecting to: http://127.0.0.1:5001` and `API key loaded: yes`.

If key is NO, run `.\setup.ps1` or copy `.env.example` to `.env`.

---

## Step 3 — Your first GET request

Add:

```python
headers = {
    "Authorization": f"Bearer {SOURCE_API_KEY}",
}

response = requests.get(
    f"{SOURCE_API_URL}/v1/incidents",
    headers=headers,
    params={"status": "open"},
    timeout=30,
)

print("Status code:", response.status_code)
```

**Run it.** Status code should be `200`.

If `401` → wrong API key. If connection error → start mock APIs.

---

## Step 4 — Handle errors properly

Replace the status print with:

```python
response.raise_for_status()
```

Add below the GET block:

```python
body = response.json()
incidents = body["data"]

print(f"Fetched {len(incidents)} open incidents")
```

**Run it.** Should say something like `Fetched 10 open incidents`.

**What you learned:** `raise_for_status()` crashes on 4xx/5xx so you don't silently use bad data.

---

## Step 5 — Explore one record

Add:

```python
first = incidents[0]
print("First incident keys:", list(first.keys()))
print("Example:", first["id"], "|", first["severity"], "|", first["facility"])
```

**Run it.** Look at the output — this is the JSON shape you'll map in integrations.

---

## Step 6 — Filter critical and high

Add:

```python
SYNC_SEVERITIES = {"critical", "high"}

filtered = []
for inc in incidents:
    if inc["severity"] in SYNC_SEVERITIES:
        filtered.append(inc)

print(f"\n{len(filtered)} incidents need attention:\n")
```

---

## Step 7 — Print a report

Add:

```python
for inc in filtered:
    print(f"  {inc['id']} | {inc['severity']:8} | {inc['facility']}")
```

**Run it.** You should see 6 lines like:
```
  INC-38192 | critical | Water Treatment Plant 4
  ...
```

---

## Step 8 — Optional: pretty summary

Add at the very bottom:

```python
if __name__ == "__main__":
    print("\nDone — this script GETs, parses JSON, and filters. That's 80% of the job.")
```

**Verify:**

```powershell
python exercises/verify/verify_03.py
```

Pass? Move to **Guide 04**.

---

## Experiment (2 min)

Change `params` to also filter by severity on the API side:

```python
params={"status": "open", "severity": "critical"},
```

**Run it.** Fewer results? The API did the filtering — sometimes better than filtering in Python.

Change it back before verify.

---

## Stuck?

<details>
<summary>ModuleNotFoundError: requests</summary>
Activate venv: `.\venv\Scripts\Activate.ps1` then `pip install -r requirements.txt`
</details>

<details>
<summary>Connection refused</summary>
Start mock APIs in another terminal: `python mock-apis/run_servers.py`
</details>
