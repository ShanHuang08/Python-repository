import requests
import json

ip = 'https://10.184.30.32'
Link = ip + '/redfish/v1/Systems'

payload = {
    "UserName": "ADMIN",
    "Password": "ADMIN",
}

header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Authorization" : "Basic QURNSU46QURNSU4=" #ADMIN / ADMIN
}

# s = requests.session().post()
r = requests.get(Link, headers=header, verify=False)

print(r.status_code)
print(type(r.text)) #str
jdata = json.loads(r.text)
print(len(jdata))
print(jdata)
