import requests
from pprint import pprint
import urllib3

# 禁用所有警告 Idea from ChatGPT
urllib3.disable_warnings()

def GET(url, auth=None, timeout=20, retries=3):
    """
    `GET()[0]` : `Status code`

    `GET()[1]` : `text`

    `GET()[-1]` : `Get_data`
    """
    try:
        Get_data = requests.get(url=url, auth=auth, verify=False, timeout=timeout)
        return [Get_data.status_code, Get_data.text, Get_data]
    except requests.exceptions.HTTPError as e:
        print(f'HTTPError: {e}')
        Retry_api(url, auth, retries)
    except requests.exceptions.ConnectTimeout as e:
        print(f'ConnectTimeout: {e}')
        Retry_api(url, auth, retries)
    except requests.exceptions.ConnectionError as e:
        print(f'ConnectionError: {e}')
        Retry_api(url, auth, retries)
    except requests.exceptions.Timeout as e:
        print(f'Timeout: {e}')
        Retry_api(url, auth, retries)

def GET_Data(url, auth):
    try:
        GET(url=url, auth=auth)
        pprint(f"HTTP Status: {GET[0]}\nBody:\n{GET[1]}")
        return GET[-1]
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
    except requests.exceptions.Timeout as e:
        print(e)

def PATCH(url, auth, body, timeout=10):
    """
    `PATCH()[0]` : `Status code`

    `PATCH()[1]` : `text`

    `PATCH()[-1]` : `json()`
    """
    try:
        Patch_data = requests.patch(url=url, auth=auth, json=body, verify=False, timeout=timeout)
        return [Patch_data.status_code, Patch_data.text, Patch_data.json()]
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
    except requests.exceptions.Timeout as e:
        print(e)

def POST(url, auth, body=None, timeout=10):
    """
    `POST()[0]` : `Status code`

    `POST()[1]` : `text`

    `POST()[-1]` : `json()`
    """
    try:
        Post_data = requests.post(url=url, auth=auth, json=body, verify=False, timeout=timeout)
        return [Post_data.status_code, Post_data.text, Post_data.json()]
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
    except requests.exceptions.Timeout as e:
        print(e)

def DELETE(url, auth):
    """
    `DELETE()[0]` : `Status code`

    `DELETE()[1]` : `text`
    """
    try:
        Delete_data = requests.delete(url=url, auth=auth, verify=False, timeout=10)
        return [Delete_data.status_code, Delete_data.text] 
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)    
    except requests.exceptions.Timeout as e:
        print(e)

def Retry_api(url, auth, retries:int):
    """Only support `GET` method"""
    import requests
    success = []
    Fail_List = []
    print(f'Start to retry {url}')
    for retry in range(1, retries+1):
        print(f'Retry {retry} times, timeout 20 secs')
        try:
            res = requests.get(url, auth, verify=False, timeout=20) # Use GET() will trigger infinity loop
        except requests.exceptions.HTTPError as e:
            print(f'HTTPError: {e}')
            continue
        except requests.exceptions.ConnectTimeout as e:
            print(f'ConnectTimeout: {e}')
            continue
        except requests.exceptions.ConnectionError as e:
            print(f'ConnectionError: {e}')
            continue
        except requests.exceptions.Timeout as e:
            print(f'Timeout: {e}')
            continue
        if res.status_code == 200: 
            print('GET api success')
            success.append(res)
            break
        else: 
            Fail_List.append(str(retry)+'. '+str(res[0]))
            continue
    if not success: 
        fail_list_str = '\n'.join(Fail_List)
        print(f"Retry api failed after {retries} times\n{fail_list_str}")