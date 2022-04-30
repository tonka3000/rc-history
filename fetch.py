import os
import json
import requests as req
from datetime import datetime

url = "https://www.raycast.com/api/v1/store_listings?per_page=2000&include_native=true"
response = req.get(url)
status = response.status_code
if status < 200 or status >= 300:
    raise Exception(f"Error with status code {status}")
j = response.json()
data = j["data"]
nd = []
for d in data:
    nd.append({
        "name": d["name"],
        "created_at" : d["created_at"],
        "updated_at": d["updated_at"],
        "download_count" : d["download_count"]
    })

now = datetime.now()

rel_folder = now.strftime("%Y/%m")
filename = now.strftime("%d") + ".json"
folder = os.path.join("data", rel_folder)
os.makedirs(folder, exist_ok=True)
with open(os.path.join(folder, filename), 'w', encoding="utf8") as f:
    f.write(json.dumps(nd, indent=2))
