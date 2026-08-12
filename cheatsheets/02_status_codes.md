# Status Codes (read this, then practice)

Every response has a **status code**. Memorize these — you'll explain them to customers and debug POCs with them.

## Success

| Code | Meaning | What you do |
|------|---------|-------------|
| **200** | OK | Use the response body |
| **201** | Created | POST worked — something new exists |
| **204** | No content | Success, but empty body |

## Your mistake (client errors)

| Code | Meaning | What you do |
|------|---------|-------------|
| **400** | Bad request | Fix the JSON / missing fields |
| **401** | Unauthorized | Fix API key / Bearer token |
| **403** | Forbidden | Key works, but no permission |
| **404** | Not found | Wrong URL or ID |
| **409** | Conflict | Duplicate — skip or update (idempotency!) |
| **429** | Rate limited | Slow down, retry later |

## Their mistake (server errors)

| Code | Meaning | What you do |
|------|---------|-------------|
| **500** | Server error | Retry later; not your payload's fault |
| **502/503** | Bad gateway / unavailable | Wait and retry |

## SE one-liners

- **401** → "Our token is missing or wrong."
- **409** → "We already created that ticket — good, no duplicate."
- **429** → "We're calling too fast; back off."
- **500** → "Their API had an issue; we'll retry."

**Next:** type these codes and meanings yourself.
