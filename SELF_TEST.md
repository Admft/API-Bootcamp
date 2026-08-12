# Samsara SE Self-Test — Mastery Capstone

Complete this **without looking at solutions or guides**. Aim for under 45 minutes of coding, then the oral demo.

You should already have finished every **review / debug / exam** gate in the course. If not, go back — this exam assumes that muscle memory.

Create everything in **`exercises/my-work/`** — type from a blank file.

## Prerequisites

- [ ] Mock APIs running (`python mock-apis/run_servers.py`)
- [ ] Blank Python file open (`exercises/my-work/self_test.py`)
- [ ] `.env` configured
- [ ] You can recite the debug ritual: error → status → Postman → env → JSON keys → one fix

## The 10 Tasks

### 1. Find authentication documentation
- [ ] Open `mock-apis/README.md` and identify auth method and keys

### 2. Make a GET request in Postman
- [ ] Import collection, send "List Open Incidents", get 200

### 3. Make the same request in Python
- [ ] GET open incidents using `requests` + Bearer token from env

### 4. Extract fields from JSON
- [ ] Print `id`, `severity`, and `facility` for each incident

### 5. Filter results
- [ ] Only show `critical` and `high` severity

### 6. Transform to another dictionary
- [ ] Map to: `external_id`, `site`, `description`, `priority`

### 7. POST that dictionary
- [ ] Create a ticket in the destination API

### 8. Handle a failed request
- [ ] POST the same ticket again; catch 409 and print a skip message

### 9. Store secrets in environment variables
- [ ] No hardcoded keys in your script

### 10. Write a README
- [ ] Use `templates/integration-readme-template.md` to document your script

## Pass Criteria

You pass only if **all** are true:

- [ ] All 10 coding tasks checked
- [ ] Script rerun is idempotent (duplicates → SKIP / 409 handled)
- [ ] You completed the course mastery gates (review + debug + exam bands)
- [ ] Oral test below is clear without reading code

Craft skills covered:

- Task automation scripting
- Transferring data between systems using APIs
- Building solutions leveraging open APIs
- Documenting for fellow Sales Engineers
- Debugging with a calm ritual instead of panic-rewrites

## Sales Engineer Oral Test

After the script works, close the code and answer these out loud:

- [ ] In 60 seconds, explain the customer problem and measurable POC success criteria
- [ ] In 60 seconds, explain `device/sensor → network → cloud → API → customer system`
- [ ] In 60 seconds, explain authentication, pagination, idempotency, timeout handling, and `409 Conflict` without jargon
- [ ] In 60 seconds, contrast `401` vs `409`, and polling vs webhooks
- [ ] In 60 seconds, state what must be validated before production: official API contracts, rate limits, data volume, security, deployment ownership, monitoring, and support
- [ ] In 60 seconds, close on business value and recommend the next POC step

## Stretch Goals

- [ ] Add pagination (fetch all pages with `limit=3`)
- [ ] Add `--dry-run` flag
- [ ] Explain each vocabulary term in `cheatsheets/vocabulary.md` out loud
- [ ] Fix one `exercises/broken/` script from memory using the debug ritual
- [ ] Adapt discovery questions for transportation, construction, or field services

## Reset for Retest

```bash
# Restart destination API to clear tickets (Ctrl+C run_servers, restart)
python mock-apis/run_servers.py
```

Delete your `self_test.py` and `self_test_README.md`, then rebuild from memory.
