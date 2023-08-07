import requests
import json

ip = '10.20.30.10'
urls = []
Link = 'https://'+ip +'/redfish/v1/Systems'
auth = ('ADMIN', 'ADMIN')

try:
    Get_data = requests.get(Link, auth=auth, verify=False)
    print(f"HTTP status: {Get_data.status_code}")
    print(Get_data.text)
except requests.exceptions.HTTPError as e:
    print(str(e))
except requests.exceptions.ConnectTimeout as e:
    print(str(e))
except requests.exceptions.ConnectionError as e:
    print(str(e))
