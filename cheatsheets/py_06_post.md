# POST Requests — Create Something

GET reads. **POST creates.**

```python
payload = {
    "external_id": "INC-38192",
    "site": "Water Treatment Plant 4",
    "description": "Pump pressure below threshold",
    "priority": 1,
}

response = requests.post(
    "http://127.0.0.1:5002/v1/tickets",
    headers={"Authorization": f"Bearer {DEST_KEY}"},
    json=payload,   # sends JSON body
    timeout=30,
)
response.raise_for_status()
print(response.status_code)  # 201 Created
print(response.json())
```

## SE tips

- Destination API uses a **different** key than the source
- `json=payload` sets the body AND Content-Type
- **201** = created; **409** = already exists (duplicate)

**Next:** POST one ticket by hand in a type-along.
