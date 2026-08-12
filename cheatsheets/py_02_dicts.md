# Python: Dictionaries (the JSON twin)

APIs speak JSON. In Python, a JSON object is a **dictionary**.

```python
incident = {
    "id": "INC-38192",
    "severity": "critical",
    "facility": "Water Treatment Plant 4",
}

print(incident["id"])         # INC-38192
print(incident["severity"])   # critical
```

## Rules

- Curly braces `{ }`
- `"key": value` pairs separated by commas
- Read a value with `dict["key"]`
- Missing key → crash — later you'll learn `.get()`

**Next:** build an incident dictionary by typing it.
