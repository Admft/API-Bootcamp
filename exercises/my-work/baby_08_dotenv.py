import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SOURCE_API_KEY")
BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")

headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get(f"{BASE}/v1/incidents", headers=headers, timeout=30)

print(response.status_code)