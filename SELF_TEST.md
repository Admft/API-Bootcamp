# Self-Test — Can You Do This From Scratch?

Complete this **without looking at solutions or guides**. Time yourself: aim for under 45 minutes.

Create everything in **`exercises/my-work/`** — type from a blank file.

## Prerequisites

- [ ] Mock APIs running (`python mock-apis/run_servers.py`)
- [ ] Blank Python file open (`exercises/my-work/self_test.py`)
- [ ] `.env` configured

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

If you checked all 10 boxes, you cover the practical meaning of:

- Task automation scripting
- Transferring data between systems using APIs
- Building solutions leveraging OpenAPIs
- Documenting for fellow Sales Engineers

## Stretch Goals

- [ ] Add pagination (fetch all pages with `limit=3`)
- [ ] Add `--dry-run` flag
- [ ] Explain each vocabulary term in `cheatsheets/vocabulary.md` out loud

## Reset for Retest

```powershell
# Restart destination API to clear tickets (Ctrl+C run_servers, restart)
python mock-apis/run_servers.py
```

Delete your `self_test.py` and `self_test_README.md`, then rebuild from memory.
