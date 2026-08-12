import requests

BASE = "http://127.0.0.1:5001"

response = requests.get(f"{BASE}/health", timeout=30)

print(response.json())