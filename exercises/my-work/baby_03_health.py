import requests

url = "http://127.0.0.1:5001/health"

response = requests.get(url, timeout=30)

print(response.status_code)