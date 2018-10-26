import requests
url = 'http://my-aiops-publisher-my-aiops2.5a9f.insights-dev.openshiftapps.com:5000'
data = '{  "platform": {    "login": {      "userName": "name",      "password": "pwd"    }  } }'
response = requests.post(url, data=data,headers={"Content-Type": "application/json"})
print(response)
print(response.text)

