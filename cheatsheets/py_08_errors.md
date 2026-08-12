# Errors Without Crashing

```python
try:
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()
except requests.Timeout:
    print("Timed out — try again later")
except requests.HTTPError as e:
    if e.response is not None and e.response.status_code == 404:
        print("Not found")
    else:
        print("HTTP error", e)
except requests.RequestException as e:
    print("Request failed", e)
```

## SE tip

A POC that crashes on one bad ID looks amateur. Catch, log, continue.

**Next:** type a safe_get that survives a missing ID.
