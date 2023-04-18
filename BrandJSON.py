import requests
import json
import time
Channel='bh'
def BE_BrandJSON():
    url='https://'+Channel+'-admin-uat.paradise-soft.com.tw/apis/bank?code=&name=&status=-1&recommend=-1&pi=1&ps=500&po=&_=1667982100630'
    headers={
        # 手動改cookie
        'cookie':'.xy-web=MTY2NDMyNTcxNXxGdkxoWGE2UDVNaEx4cWFWQ1NoN0p4UFd5NTIwTWREVU9xb2t0alZ2MThrSUttc1NfdHdHQ1lrc2hyUDZfMUhBcUI1MDd4SUp1V0VBbncyaHJzWDNLMVNYNTlhM3czRFdTVmJSMi1mbXV4TERtall6UW9VNmFldnYwbzMxQ1ZzSjFCVnQtamtBb2pBWmM5c05SNU1OWEVHR0dHQWhaMHhKeWN3M3RlMGxqRXhQQ0JxbUlZczZFbjVrbkhaVFM5TDVmVlNaR09GTGk1MGNYMno0RzY1OWRuQ0N4U1RNdENtTlM0UnpJc0hPdFpWV2NCckhPYXVtc3c9PXxkW-eJCT4HOdCMo8MkWthVjbWcgY1xm-3ftJI0PK5eCw==; .xy-admin=MTY2Nzk4MjA5NHxDMkw5bHd0N3pPSGt0bzZMVW5Sa2kyY01qWlIzVnVXZnlVNjNwbl9HR3JENUFMaE8xRkJZQ0JFbE8xM2NiUUV0dkNhck03VV9wWVRsU2xGVW1xSkEyQ1ByTG1YSGVDLTlfN2l4dkpXTGJZbGsydW5JRVgtMVBvOHpraEpBVnkxVnNXLWRkcDlXQkxzT3F4Tl9WRGZvQ2JwbnNsLXgwNU41VTBvSWE1X2Z3R1pHSWVUNjdkZ0ZWU2RwZWFob3RlT2t2cnpkZmRrNV83dk4xTlhOZmdFRnBZMU1vWmVRMW5BPXx5qTmhHRopObGzbyZOFP7HMpE0uybLwO0dPRIh_GYtKA==',
        'referer':'https://bh-admin-uat.paradise-soft.com.tw/bank',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'accept':'application/json, text/javascript, */*; q=0.01',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with':'XMLHttpRequest'
    }

    data=requests.get(url,headers=headers).text
    # print(len(data))
    jdata=json.loads(data)
    print('jdata total='+str(jdata['Pager']['Total']))
    # print(jdata['Items'][0:3])
    return jdata

def FE_transfer():
    transfer_url='https://'+Channel+'-web-uat.paradise-soft.com.tw/my/transfer'
    transfer_api='https://'+Channel+'-web-uat.paradise-soft.com.tw/apis/my/wallet/transfer'
    balance_api='https://'+Channel+'-web-uat.paradise-soft.com.tw/apis/my/wallet/balance?&_=1667984511049'
    WalletFrom='cp'
    WalletTo='kk'
    amount='10'
    payload={
        'from':WalletFrom,
        'to':WalletTo,
        'amount':amount
    }
    headers={
        'accept':'application/json, text/javascript, */*; q=0.01',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-TW,zh;q=0.9',
        'ontent-length':'23',
        'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie':'Hm_lvt_ca4875a2d78d98cace56a96514e152a8=1667984408; popupBillboard=2020-10-30%2016%3A53%3A47; quick_ui_right=1; quick_ui_left=1; setCookie=1667984505550; .xy-web=MTY2Nzk4NDUwNXxHclo4dDdablh5emlUWEFrbWV5eTV6eGFFM2lIWmI3Y1I1Q20tVjJlcmFHRzkxZ1pHMjNNQ2h1YUxJbU8yQ0lhRVdNenk3OVdTb1l2clJPRFE3Ukd3THIwcHV6ejlTMzF2enNMVWhOSDhBQ014TmVsMmktZUdPVUExeldGTWg3OWxzQS1DNlozblI4Z3pvaVByYUU4OGJuMmhiNzVsQWZSNmxHMmhZeFF2bDhlajg4QmhjTzNtRzMtcEdRcVZGLW1hSlJ5MUtMM3pfWDEzczhaMGltLUg1emNDQ1B4WEtFN0d4REdudndBejdfVGduZXlDbkU9fKw-tmqoacp0xz2EE88TPDa49_BmekAR1-HcrJN25vG-; has_check_passwd=1; Hm_lpvt_ca4875a2d78d98cace56a96514e152a8=1667984511; referer=MTY2Nzk4NDU0MXxrS0NZb0p5X29yWWpnaVdpajVHd2ZuWXBsWmZTTXU4cVdDYjJnMS11ZG8wUnV5ZGI0TFVuZ3VKSWR2ZE1jVWRnWTUtRFNTa2dJYnR2UzI1ckVlMTA5bGRNbjRlcXzcRlfnJ4HzCyYnolEKDQ2I93tQr5LVdXX48mC_CkTDqA%3D%3D',
        'origin':'https://'+Channel+'-web-uat.paradise-soft.com.tw',
        'referer':transfer_url,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-requested-with':'XMLHttpRequest'
    }

    WalletTransfer=requests.post(transfer_api, data=payload, headers=headers)
    print(WalletTransfer.text) #api回傳狀態
    time.sleep(5)
    GetBalance=requests.get(balance_api, headers=headers).text
    jdata=json.loads(GetBalance)
    print('帳號='+jdata[0]['memberlogin'])
    Wallets=[]
    for i in range(len(jdata)):
        if jdata[i]['walletcode'] in [WalletFrom, WalletTo]:
            Wallets.append(jdata[i]['walletname']+' ('+jdata[i]['walletcode']+'):'+str(jdata[i]['balance']))
    for j in range(len(Wallets)):
        print(Wallets[j])

if __name__=='__main__':
    # BE_BrandJSON()
    FE_transfer()

