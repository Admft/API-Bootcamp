# Debug Ritual (memorize this)

When a script fails, do **not** rewrite everything. Walk the checklist:

1. **Read the error** — last line of the traceback usually names the problem.
2. **Status code?** — `401` auth, `404` URL/ID, `409` duplicate, `500` their side.
3. **Postman first** — if Postman fails, Python will fail the same way.
4. **Check `.env`** — is the key loaded? Did you call `load_dotenv()`?
5. **Check JSON keys** — `facility` vs `site`, `data` list vs object.
6. **Timeouts** — always pass `timeout=30`.
7. **Fix one thing** — re-run after each change.

Broken starters in this course live under `exercises/broken/`. Your job is to repair them until Analyze is green.
