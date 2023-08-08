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
    return [Get_data.status_code, Get_data.text]

def PATCH(url, auth, body):
    try:
        Patch_data = requests.patch(url=url, auth=auth, json=body, verify=False)
    except requests.exceptions.HTTPError as e:
        print(str(e))
    except requests.exceptions.ConnectTimeout as e:
        print(str(e))
    except requests.exceptions.ConnectionError as e:
        print(str(e))
    if Patch_data.status_code == 200:
        return Patch_data.status_code
    else:
        return f"{Patch_data.status_code}\nBody: {Patch_data.text}"

def POST(url, auth, body):
    try:
        Post_data = requests.post(url=url, auth=auth, json=body, verify=False)
    except requests.exceptions.HTTPError as e:
        print(str(e))
    except requests.exceptions.ConnectTimeout as e:
        print(str(e))
    except requests.exceptions.ConnectionError as e:
        print(str(e))
    if Post_data.status_code == 201:
        return Post_data.status_code
    else:
        return f"{Post_data.status_code}\nBody: {Post_data.text}"

def DELETE(url, auth):
    try:
        Delete_data = requests.delete(url=url, auth=auth, verify=False)
    except requests.exceptions.HTTPError as e:
        print(str(e))
    except requests.exceptions.ConnectTimeout as e:
        print(str(e))
    except requests.exceptions.ConnectionError as e:
        print(str(e))        
    if Delete_data.status_code == 200:
        return Delete_data.status_code
    else:
        return f"{Delete_data.status_code}\nBody: {Delete_data.text}"