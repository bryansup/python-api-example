import requests
import json

url_endpoint = "http://127.0.0.1:5000/uppercase"
resp = requests.get(url_endpoint, params = {"text" : "this is some text"})

print(resp.json())
print(resp.status_code)