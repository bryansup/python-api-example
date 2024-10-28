import requests
import json

#url_endpoint = "http://127.0.0.1:5000/uppercase"
url_endpoint = "https://learning-api-app.onrender.com/generator"

resp = requests.get(url_endpoint, params = {"message" : "I ","duplication_factor" : 4})

print(resp.json())
print(resp.status_code)