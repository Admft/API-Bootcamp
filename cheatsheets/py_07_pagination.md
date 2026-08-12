# Pagination — When There Are Too Many Pages

APIs rarely return everything at once. They return a **page**.

```json
{
  "data": [ ... ],
  "pagination": { "page": 1, "limit": 3, "has_more": true }
}
```

```python
all_rows = []
page = 1
while True:
    body = requests.get(url, params={"page": page, "limit": 3}, ...).json()
    all_rows.extend(body["data"])
    if not body["pagination"]["has_more"]:
        break
    page += 1
```

**Why SEs care:** a fleet with 10,000 assets won't fit in one response.

**Next:** type a pagination loop with `limit=2`.
