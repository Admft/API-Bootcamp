# Python: Functions (reusable recipes)

A **function** is a named recipe you can call again.

```python
def severity_to_priority(severity):
    mapping = {
        "critical": 1,
        "high": 2,
        "medium": 3,
        "low": 4,
    }
    return mapping[severity]


print(severity_to_priority("critical"))  # 1
```

Transform one API shape into another:

```python
def transform_incident(incident):
    return {
        "external_id": incident["id"],
        "site": incident["facility"],
        "description": incident["message"],
        "priority": severity_to_priority(incident["severity"]),
    }
```

**Next:** type a tiny function, then a transform.
