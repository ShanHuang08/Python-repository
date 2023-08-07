import requests
import json
from pprint import pprint

# ip = '10.184.16.44'
urls = []
# Link = 'https://'+ip +'/redfish/v1/Systems/1'
# auth = ('ADMIN', 'ADMIN')
def GET(Link, auth):
    try:
        Get_data = requests.get(Link, auth=auth, verify=False)
        print(f"HTTP status: {Get_data.status_code}\nBody:\n")
        pprint(Get_data.text)
        # 尋找特定str是否有符合預期
    except requests.exceptions.HTTPError as e:
        print(str(e))
    except requests.exceptions.ConnectTimeout as e:
        print(str(e))
    except requests.exceptions.ConnectionError as e:
        print(str(e))

# GET(Link, auth)
# PATCH(Link, auth, body)
# PUSH(Link, auth, body)