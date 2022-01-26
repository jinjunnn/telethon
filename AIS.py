import requests
import json

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6eyJpZCI6IjE3NDMiLCJuYW1lIjoiTWFyaW5lIE9ubGluZSIsInV1aWQiOiIxNzQzIn0sImlzcyI6InNwaXJlLmNvbSIsImlhdCI6MTYzMTI1NzI3NX0.s-OXE_zhb5EYWqvTt0bL6gfW4X8tbnn-UIkdZSyYkyE'
endpoint = 'https://ais.spire.com/vessels'
headers = {"Authorization": "Bearer " + token,'Accept':'application/json'}
content = {
    'mmsi':'574012723',
    'limit':'100',
}
r = requests.get(url=endpoint,params=content,headers=headers)
print(json.dumps(r.json(), indent=4, ensure_ascii=False))