# Postman Exercise (30 min)

Postman is for **exploring** APIs before you automate them. You don't need to master it — just enough to test requests manually.

## Setup

1. Download Postman: https://www.postman.com/downloads/
2. Import the collection: **File → Import →** select `postman/mock-apis.postman_collection.json`
3. Start mock APIs: `python mock-apis/run_servers.py`

## Exercise 01b — Manual API Calls

Work through each request in the collection **in order**. For each one:

1. Click Send
2. Check the status code (should be 200 or 201)
3. Inspect the JSON response body
4. Note which headers were sent

### Requests to complete

| # | Request | What to notice |
|---|---------|----------------|
| 1 | Health — Source | No auth needed |
| 2 | List Open Incidents | Bearer token in Authorization tab |
| 3 | Filter Critical Incidents | Query params: `status=open&severity=critical` |
| 4 | Get Single Incident | Path variable `{incident_id}` |
| 5 | Paginated Incidents | `limit=3` forces multiple pages |
| 6 | Create Ticket | POST with JSON body |
| 7 | Duplicate Ticket (409) | Run #6 again — see Conflict |
| 8 | List All Tickets | Verify tickets from #6 |

## After Postman Works

Pick request #2 (List Open Incidents). Open `exercises/03_get_and_filter.py` and recreate that exact request in Python.

That's the workflow: **Docs → Postman → Python → Automate**.

## Optional: Export to Code

In Postman, after a successful request:
- Click **Code** (right sidebar, `</>` icon)
- Select **Python — Requests**
- Compare generated code to our exercises

The generated code is a starting point — you'll add filtering, transforms, and error handling.
