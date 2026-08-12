# Reading API Docs (SE habit)

Before you open Postman or write Python, extract four facts from the docs:

1. **Method** — GET, POST, PUT, PATCH, DELETE
2. **Path** — e.g. `/v1/incidents`, `/health`
3. **Auth** — none, Bearer, API key header, OAuth…
4. **Gotchas** — query params, pagination fields, `409` on duplicates, rate limits

## This course's docs

Open [`mock-apis/README.md`](../mock-apis/README.md):

| Need | Look for |
|------|----------|
| Is the API up? | `GET /health` — no auth |
| List alerts | `GET /v1/incidents` — Bearer **source** key |
| Create work | `POST /v1/tickets` — Bearer **dest** key; `409` if `external_id` exists |

## Ritual

Docs → Postman (prove it) → Python (automate it) → debug ritual if it fails.
