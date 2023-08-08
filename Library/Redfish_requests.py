import requests
from pprint import pprint

def GET(url, auth):
    try:
        Get_data = requests.get(url=url, auth=auth, verify=False)
        print(f"HTTP Status: {Get_data.status_code}\nBody:\n")
        pprint(Get_data.text)
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
    return [Patch_data.status_code, Patch_data.text]

def POST(url, auth, body):
    try:
        Post_data = requests.post(url=url, auth=auth, json=body, verify=False)
    except requests.exceptions.HTTPError as e:
        print(str(e))
    except requests.exceptions.ConnectTimeout as e:
        print(str(e))
    except requests.exceptions.ConnectionError as e:
        print(str(e))
    return [Post_data.status_code, Post_data.text]

def DELETE(url, auth):
    try:
        Delete_data = requests.delete(url=url, auth=auth, verify=False)
    except requests.exceptions.HTTPError as e:
        print(str(e))
    except requests.exceptions.ConnectTimeout as e:
        print(str(e))
    except requests.exceptions.ConnectionError as e:
        print(str(e))      
    return [Delete_data.status_code, Delete_data.text]  