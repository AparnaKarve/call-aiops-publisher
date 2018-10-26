import requests
url = 'http://127.0.0.1:5000'
data = '{  "platform": {    "login": {      "userName": "name",      "password": "pwd"    }  } }'
response = requests.post(url, data=data,headers={"Content-Type": "application/json"})
print(response)
print(response.text)

