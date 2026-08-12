# HTTP Methods (read this, then practice)

An API call is just a message with a **method** (what you want to do) and a **URL** (where).

| Method | Purpose | Think of it as |
|--------|---------|----------------|
| **GET** | Retrieve data | "Show me…" |
| **POST** | Create something | "Make a new…" |
| **PUT** | Replace entirely | "Overwrite with…" |
| **PATCH** | Partial update | "Change just this field…" |
| **DELETE** | Remove something | "Throw away…" |

## In Python (you'll type this soon)

```python
requests.get(url)                 # GET
requests.post(url, json=data)     # POST
requests.put(url, json=data)      # PUT
requests.patch(url, json=data)    # PATCH
requests.delete(url)              # DELETE
```

## Remember

- **GET** should not create or change data. Use it to read.
- **POST** is how you create tickets, work orders, etc.
- You will use **GET** and **POST** constantly as a Sales Engineer building integrations.

**Next:** a tiny type-along where you type these meanings yourself so they stick.
