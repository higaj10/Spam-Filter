import json
import requests
# url = "http://127.0.0.1:5000/predict"
url = "http://127.0.0.1:5000/predict"
payload = input("Enter a String : \t")
# payload = {"text":"this is mail"}
r = requests.post(url , data=json.dumps(payload))
print(r.text)
