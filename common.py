import os
import re
import json
from datetime import datetime, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def get_extensions_history(folder:str, data=[]):
    now = datetime.now()
    past = now - timedelta(days=14)
    result = []
    for ext in data:
        ext_name = ext["name"]
        downloads = []
        for date in daterange(past, now):
            filename = os.path.join(folder, date.strftime("%Y/%m/%d.json"))
            if os.path.exists(filename):
                with open (filename, 'r', encoding="utf8") as f:
                    file_data =json.load(f)
                    for e in file_data:
                        if e["name"] == ext_name:
                            downloads.append(e["download_count"])
        result.append({
            "name" : ext_name,
            "previous_days_downloads" : downloads
        })
    return result
