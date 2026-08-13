import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SOURCE_API_KEY")
BASE = os.getenv("SOURCE_API_URL", "http://127.0.0.1:5001")
headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get(
    f"{BASE}/v1/incidents",
    headers = headers,
    params={"status": "open"},
    timeout=30
)
response.raise_for_status()
data = response.json()

for incident in data["data"]:
    pass
    
for incident in data["data"]:
    print(incident["id"], incident["severity"], incident["facility"])