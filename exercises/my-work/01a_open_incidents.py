import os 
import requests
from dotenv import load_dotenv

load_dotenv()

SOURCE_API_KEY = os.getenv("SOURCE_API_KEY")

SOURCE_API_URL = os.getenv("SOURCE_API_URl", "http://127.0.0.1:5001")

response = requests.get(
    f"{SOURCE_API_URL}/v1/incidents",
    headers={"Authorization": f"Bearer {SOURCE_API_KEY}"},
    params={"status": "open"},
    timeout=30,
)

response.raise_for_status()

data = response.json()

print("Count", len(data["data"]))

print("Count:", len(data["data"]))

