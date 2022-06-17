import requests
import time
import json

data = {'name': 'germey', 'age': '22'}

while True:
    for data_type in ['car', 'singal']:
        timestamp = int(time.time() * 1000)
        print(timestamp)
        response = requests.post(f"http://127.0.0.1:8080/data/?type={data_type}&timestamp={timestamp}", json=json.dumps(data))
        # print(response.text)
    time.sleep(0.3)