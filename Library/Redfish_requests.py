import requests
from pprint import pprint
import urllib3

# 禁用所有警告 Idea from ChatGPT
urllib3.disable_warnings()

def GET(url, auth):
    """
    `GET()[0]` : `Status code`

    `GET()[1]` : `text`

    `GET()[-1]` : `json()`
    """
    Get_data = None
    try:
        Get_data = requests.get(url=url, auth=auth, verify=False)
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
    if Get_data is not None:
        return [Get_data.status_code, Get_data.text, Get_data.json()]
    else:
        return Get_data

def GET_Data(url, auth):
    Get_data = None
    try:
        Get_data = requests.get(url=url, auth=auth, verify=False)
        print(f"HTTP Status: {Get_data.status_code}\nBody:\n")
        pprint(Get_data.text)
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
    if Get_data is not None:
        return [Get_data.status_code, Get_data.text]
    else:
        return Get_data

def PATCH(url, auth, body):
    """
    `PATCH()[0]` : `Status code`

    `PATCH()[1]` : `text`

    `PATCH()[-1]` : `json()`
    """
    Patch_data = None
    try:
        Patch_data = requests.patch(url=url, auth=auth, json=body, verify=False)
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
    if Patch_data is not None:
        return [Patch_data.status_code, Patch_data.text, Patch_data.json()]
    else:
        return Patch_data

def POST(url, auth, body=None):
    """
    `POST()[0]` : `Status code`

    `POST()[1]` : `text`

    `POST()[-1]` : `json()`
    """
    Post_data = None
    try:
        Post_data = requests.post(url=url, auth=auth, json=body, verify=False)
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
    if Post_data is not None:
        return [Post_data.status_code, Post_data.text, Post_data.json()]
    else:
        return Post_data

def DELETE(url, auth):
    """
    `DELETE()[0]` : `Status code`

    `DELETE()[1]` : `text`
    """
    Delete_data = None
    try:
        Delete_data = requests.delete(url=url, auth=auth, verify=False)
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)    
    if Delete_data is not None:
        return [Delete_data.status_code, Delete_data.text]  
    else:
        return Delete_data