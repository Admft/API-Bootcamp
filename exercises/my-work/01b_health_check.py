import requests
BASE_URL = "http://127.0.0.1:5001"

url = f"{BASE_URL}/health"

response = requests.get(url, timeout=30)

print(response.status_code)

response.raise_for_status()

body = response.json()

print("Service:", body["service"])

print("Service:", body["service"])