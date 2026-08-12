# Postman — Click the API Before You Code

Postman lets you send HTTP requests with buttons. Use it to prove the API works **before** writing Python.

## Flow

1. Import `postman/mock-apis.postman_collection.json`
2. Confirm mock APIs are green in the course sidebar
3. Send **Health** — expect 200, no auth
4. Send **List open incidents** — Bearer token
5. Send **Create ticket** — expect 201
6. Send create again — expect **409 Conflict**

## Why this matters for SEs

In a customer meeting you can open Postman, hit an endpoint, and show the JSON live. Then say: "I'll automate this exact call in Python."

**Next:** walk the checklist labs one request at a time.
