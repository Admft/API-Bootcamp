import os
import requests

API_KEY = os.getenv("SOURCE_API_KEY")

headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.get(
    "http://127.0.0.1:5001/v1/incidents",
    headers=headers,
    timeout=30,
)
print(response.status_code)
