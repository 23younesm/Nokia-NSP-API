import requests
import json
import urllib3

serverip = '<SERVER_IP>'
urllib3.disable_warnings()
url = "https://"+serverip+"/rest-gateway/rest/api/v1/auth/token"

payload = json.dumps({
  "grant_type": "refresh_token",
  "refresh_token": "<REFRESH_TOKEN>"
})
headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Basic <TOKEN>'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)

