# Python: if / else (decisions)

```python
severity = "critical"

if severity == "critical":
    print("Page someone now")
elif severity == "high":
    print("Create a ticket today")
else:
    print("Log it for later")
```

## Compare carefully

| Code | Meaning |
|------|---------|
| `==` | equal to |
| `!=` | not equal |
| `in` | contained in a set/list |

```python
if severity in {"critical", "high"}:
    print("Sync this one")
```

**Next:** type an if that only prints critical/high.
