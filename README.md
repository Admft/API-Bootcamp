# Samsara Sales Engineer API & Python Bootcamp

**Target role:** Sales Engineer — Mid-Market Southeast  
**Goal:** Read API docs → discover the customer need → authenticate → call endpoints → transform JSON → sync systems → document and demo the business outcome.

This course is designed around the role described in `JobDescription.txt`, especially:

- Writing reusable scripts against an open API
- Automating data transfer between business systems with Python
- Building and presenting proof-of-concept integrations
- Connecting IoT/operational events to customer workflows
- Explaining cloud, networking, authentication, and integration concepts to non-technical stakeholders
- Producing documentation another Sales Engineer can reuse

> **Training boundary:** The local endpoints and data in this repository are fictional. They simulate a connected-operations platform and a customer work-order system; they are not official Samsara API endpoints or schemas.

---

## Start the course (recommended)

```powershell
cd "c:\Users\amoffat\Documents\Documents\Projects\Learn Python"
.\setup.ps1
.\venv\Scripts\Activate.ps1

# Terminal 1 — mock APIs
python mock-apis\run_servers.py

# Terminal 2 — course platform
python course\app.py
```

Open **http://127.0.0.1:8080** — interactive lessons, built-in code editor, progress tracking, and verify buttons.

---

## Today's Schedule

| Time | Block | File(s) | Outcome |
|------|-------|---------|---------|
| **8:00–9:00** | HTTP + APIs | `guides/01_http_type_along.md` — **type** answers + first script | Methods, status codes, first GET |
| **9:00–10:00** | Postman | `postman/README.md`, import collection | Manual API calls, inspect responses |
| **10:00–11:00** | Python basics | `guides/02_python_type_along.md` → `my-work/02_basics.py` | Dicts, loops, transform |
| **11:00–12:00** | Script #1 | `guides/03_get_filter_type_along.md` → `my-work/03_get_incidents.py` | Retrieve + filter |
| **12:00–1:30** | Script #2 | `guides/04_sync_type_along.md` → `my-work/04_sync.py` | System A → B |
| **1:30–2:30** | Reliability | `guides/05_reliability_type_along.md` → `my-work/05_reliability.py` | Pagination, errors |
| **2:30–3:30** | Bash/JS recognition | `cheatsheets/http-api-basics.md` (bottom section) | Same HTTP, different syntax |
| **3:30–6:00** | Capstone | `guides/06_capstone_type_along.md` → `my-work/06_sync_incidents.py` | Full integration you typed |
| **6:00–7:00** | Document + demo | `capstone/README.md`, `ROLE_PLAYBOOK.md` | SE-ready documentation and a customer-facing demo |
| **7:00+** | Self-test | `SELF_TEST.md` | Rebuild and explain from a blank screen |

**Rule:** ~3 hours learning, rest **building**. Type every line yourself — run after each step.

**Start here:** `exercises/START_HERE.md`  
**Keep the role lens open:** `ROLE_PLAYBOOK.md`

---

## Project Structure

```
Learn Python/
├── README.md                 ← You are here (schedule + strategy)
├── ROLE_PLAYBOOK.md          ← Discovery, demo, value, and interview practice
├── SELF_TEST.md              ← Final exam — do this tonight
├── setup.ps1                 ← One-command setup
├── requirements.txt
├── .env.example              ← Copy to .env
│
├── cheatsheets/              ← Keep open while coding
│   ├── http-api-basics.md
│   ├── python-api-syntax.md
│   └── vocabulary.md
│
├── mock-apis/                ← Local source + destination APIs
│   ├── run_servers.py        ← Start both servers
│   ├── source_api.py         ← Monitoring/incidents (port 5001)
│   └── destination_api.py    ← Ticketing (port 5002)
│
├── course/                   ← Web course platform (python course/app.py)
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── exercises/
│   ├── guides/               ← Type-along content (shown in course UI)
│   ├── my-work/              ← Your scripts (editor saves here)
│   └── verify/               ← Lesson checkers
│
├── solutions/                ← Peek only when stuck
│   └── exercises/
│
├── capstone/                 ← Production-style integration
│   ├── sync_incidents.py
│   └── README.md
│
├── postman/                  ← Import into Postman app
│   └── mock-apis.postman_collection.json
│
└── templates/
    └── integration-readme-template.md
```

---

## Priority Pyramid

If you're running out of time, study in this order — **don't reverse it:**

```
                         nice
                      ┌────────┐
                      │Bash/JS │
                   ┌──┴────────┴──┐
                   │ Logging/retry │
                ┌──┴───────────────┴──┐
                │ Pagination + errors  │
             ┌──┴──────────────────────┴──┐
             │ Python requests + JSON      │
          ┌──┴─────────────────────────────┴──┐
          │ HTTP + API docs + authentication   │
       ┌──┴────────────────────────────────────┴──┐
       │ Discovery → business value → clear demo  │
       └──────────────────────────────────────────┘
                       MUST SHOW
```

---

## The Core Pattern (memorize this)

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# 1. Auth from environment
API_KEY = os.getenv("SOURCE_API_KEY")

# 2. GET from source
response = requests.get(
    url,
    headers={"Authorization": f"Bearer {API_KEY}"},
    params={"status": "open"},
    timeout=30,
)
response.raise_for_status()
incidents = response.json()["data"]

# 3. Filter + transform
for incident in incidents:
    if incident["severity"] not in {"critical", "high"}:
        continue

    ticket = {
        "external_id": incident["id"],
        "site": incident["facility"],
        "description": incident["message"],
        "priority": 1 if incident["severity"] == "critical" else 2,
    }

    # 4. POST to destination
    result = requests.post(
        dest_url,
        headers={"Authorization": f"Bearer {os.getenv('DESTINATION_API_KEY')}"},
        json=ticket,
        timeout=30,
    )
    result.raise_for_status()
```

That's the technical pattern: **GET → filter → transform → POST → handle errors → document.**

For this Sales Engineer role, the complete pattern is:

**discover the workflow → define success → build the smallest useful integration → demo the outcome → explain deployment and risk**

---

## When You're Stuck

1. Check `cheatsheets/` for syntax
2. Test the request in Postman first
3. Look at `solutions/exercises/` for that exercise only
4. Read the mock API docs: `mock-apis/README.md`

---

## Your Pitch (after today)

> "I built a lightweight proof of concept for a connected-operations customer. It retrieves high-priority operational events through an open API, maps them into the customer's work-order schema, and creates actionable tickets without duplicates. I can explain the authentication, data flow, failure handling, and deployment assumptions, and I documented the script so another Sales Engineer can reuse it. The business outcome is a faster, more consistent response to safety and maintenance events."

---

## Tonight's Final Test

Open `SELF_TEST.md`. Rebuild the integration from scratch without looking at solutions.

You are ready when you can both build the integration and deliver the five-minute customer demo in `ROLE_PLAYBOOK.md`.
