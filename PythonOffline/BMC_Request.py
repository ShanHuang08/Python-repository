import requests

ip = '10.184.30.32'
url = 'https://' + ip
payload={
    "username" : "ADMIN",
    "password" : "ADMIN"
}

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
r = requests.session().get(url, headers=headers, data=payload, verify=False)
try:
    if r.status_code == 200:
        print(r.status_code)
except TimeoutError as t:
    print(f'TimeoutError')
except Exception as e:
    print('Exception')