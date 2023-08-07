import requests
from pprint import pprint

def GET(url, auth):
    try:
        Get_data = requests.get(url=url, auth=auth, verify=False)
        print(f"HTTP Status: {Get_data.status_code}\nBody:\n")
        pprint(Get_data.text)
        # 尋找特定str是否有符合預期
    except requests.exceptions.HTTPError as e:
        print(str(e))
    except requests.exceptions.ConnectTimeout as e:
        print(str(e))
    except requests.exceptions.ConnectionError as e:
        print(str(e))

def PATCH(url, auth, body):
    try:
        Patch_data = requests.patch(url=url, auth=auth, json=body, verify=False)
        print(f"HTTP Status: {Patch_data.status_code}")
    except requests.exceptions.HTTPError as e:
        print(str(e))
    except requests.exceptions.ConnectTimeout as e:
        print(str(e))
    except requests.exceptions.ConnectionError as e:
        print(str(e))

def POST(url, auth, body):
    try:
        Post_data = requests.post(url=url, auth=auth, json=body, verify=False)
        print(f"HTTP Status: {Post_data.status_code}")
    except requests.exceptions.HTTPError as e:
        print(str(e))
    except requests.exceptions.ConnectTimeout as e:
        print(str(e))
    except requests.exceptions.ConnectionError as e:
        print(str(e))
