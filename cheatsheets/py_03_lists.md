# Python: Lists and for-loops

A **list** holds many items in order.

```python
severities = ["critical", "high", "medium", "low"]

for severity in severities:
    print(severity)
```

A list of dictionaries (exactly like an API `data` array):

```python
incidents = [
    {"id": "INC-1", "severity": "critical"},
    {"id": "INC-2", "severity": "low"},
]

for incident in incidents:
    print(incident["id"], incident["severity"])
```

**Next:** type a list and loop it.
