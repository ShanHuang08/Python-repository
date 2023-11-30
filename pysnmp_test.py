from pysnmp.hlapi import *
from pysnmp.proto import rfc1902
from Library.Redfish_requests import *
from Library.dictionary import redfish, OID
from sys import exit
from Library.Call_Method import Check_PWD

# Source:ChatGPT 2023/8/8

server_ip = '10.184.29.186'
port = 161
Get_Only = False
oid = "1.3.6.1.4.1.21317.1.10.0"
uid_on = OID['uid on']
uid_off = OID['uid off']
Change = "Blinking"  #For Redfish 
account = 'SnmpUser'
community_key='Public'
v3_key = 'Aa123456' #MD5/DES
Account_Enable = True
auth = Check_PWD(server_ip, unique='FFSTEPBSVQ')

def snmpv2_test(server_ip, port, community_key, oid, value=None):
    # 定義 SNMP Community 和 SNMP 版本
    community = CommunityData(community_key, mpModel=1)
    # 定義目標設備
    target = UdpTransportTarget((server_ip, port))
    # 定義 SNMP 請求的 OID
    if value == None:
        oid_obj = ObjectType(ObjectIdentity(oid))
        # 建立 SNMP GET 請求
        get_request = getCmd(SnmpEngine(), community, target, ContextData(), oid_obj)
        error_indication, error_status, error_index, var_binds = next(get_request)
        print(f'SNMPv2 Get:\nLog: {var_binds}')
        # 處理回應結果
        if error_indication:
            print(f"Error: {error_indication}, Please enable SNMP and set-up community!")
        elif error_status:
            print(f"Error: {error_status} at {error_index and var_binds[int(error_index)-1][0] or '?'}")
        else:
            for var_bind in var_binds:
                # 取得 SNMP 回傳的值
                print(f'OID: {var_bind[0]}, Value: {var_bind[-1]}')
    else:
        oid_obj = ObjectType(ObjectIdentity(oid), value)
        # 建立 SNMP SET 請求
        set_request = setCmd(SnmpEngine(), community, target, ContextData(), oid_obj)
        error_indication, error_status, error_index, var_binds = next(set_request)
        print(f'SNMPv2 Set:\nLog: {var_binds}')

        if error_indication:
            print(f"Error: {error_indication}, Please enable SNMP and set-up community!")
        elif error_status:
            print(f"Error: {error_status} at {error_index and var_binds[int(error_index)-1][0] or '?'}")
        else:
            for var_bind in var_binds:
                print(f'OID: {var_bind[0]}, Value: {var_bind[-1]}')        

def snmpv3_test(server_ip, port, account, v3_key, oid, value=None):
    MD5_DES_credential = UsmUserData(userName=account, authKey=v3_key, privKey=v3_key, authProtocol=usmHMACMD5AuthProtocol, privProtocol=usmDESPrivProtocol)
    target = UdpTransportTarget((server_ip, port))
    if value == None:
        oid_obj = ObjectType(ObjectIdentity(oid))
        get_request = getCmd(SnmpEngine(), MD5_DES_credential, target, ContextData(), oid_obj)
        error_indication, error_status, error_index, var_binds = next(get_request)
        print(f'SNMPv3 Get:\nLog: {var_binds}')

        if error_indication:
            print(f"Error: {error_indication}")
        elif error_status:
            print(f"Error: {error_status} at {error_index and var_binds[int(error_index)-1][0] or '?'}")
        else:
            for var_bind in var_binds:
                value = var_bind[-1]
                print(f'OID: {var_bind[0]}, Value: {value}')
    else:
        oid_obj = ObjectType(ObjectIdentity(oid), value)
        set_request = setCmd(SnmpEngine(), MD5_DES_credential, target, ContextData(), oid_obj)
        error_indication, error_status, error_index, var_binds = next(set_request)
        print(f'SNMPv3 Set:\nLog: {var_binds}')

        if error_indication:
            print(f"Error: {error_indication}")
        elif error_status:
            print(f"Error: {error_status} at {error_index and var_binds[int(error_index)-1][0] or '?'}")
        else:
            for var_bind in var_binds:
                value = var_bind[-1]
                print(f'OID: {var_bind[0]}, Value: {value}')

def Redfish_setup(Disable_Account=None):
    print('Start setting up SNMP environment')
    Create = POST(url='https://'+server_ip+ redfish['Accounts'], auth=auth, body=redfish['MD5_DES'])
    if Create[0] == 201:
        print('Account has created')
    else:
        print(f'Failed, Status code: {Create[0]}\n{Create[-1]}')
        if "reached the limit" in Create[1]:
            Get_Account = GET(url='https://'+server_ip+'/redfish/v1/AccountService/Accounts/16', auth=auth)
            if Get_Account[0] == 200:
                print("Accounts reach the limit, Please delete an account and try again")
        exit()
    
    bodies =[redfish['Enable SNMP'], redfish['Add SNMPv2 Community'], redfish['Enable SNMPv3']]
    for body in bodies:
        Snmp = PATCH(url='https://'+server_ip + redfish['SNMP'], auth=auth, body=body)
        if Snmp[0] not in [200,202]:
             print(f'SNMP set-up failed\nStatus: {Snmp[0]}\n{Snmp[1]}')
             exit()

def UID_Change(Change):
    body = {"IndicatorLED" : Change}
    uid_patch = PATCH(url='https://'+server_ip+ redfish['Systems'], auth=auth, body=body)
    if uid_patch[0] == 200 and Change == "Blinking":
        print('UID Control enable')
    elif uid_patch[0] == 200 and Change == "Off":
        print('UID Control disable')
    else:
        print(f'Failed, Status: {uid_patch[0]}\n Body:{uid_patch[1]}')

def Disable_Account(Account_Enable=None):
    if Account_Enable == False:
        print('Disable account')
        jdata = GET(url='https://'+server_ip+ redfish['Accounts'], auth=auth)[-1].json()
        count = str(jdata['Members@odata.count']+1)
        redfish['MD5_DES']['Enabled'] = Account_Enable
        Modify = PATCH(url='https://'+server_ip+ redfish['Accounts'] + count, auth=auth, body=redfish['MD5_DES'])
        if Modify[0] == 200:
            print('Account has disabled')
        else:
            print(f'Failed, Status code: {Modify[0]}\n{Modify[-1]}')
    else:
        pass

def Clear_setup():
    print('Clear SNMP environment')
    Disable_SNMP = PATCH(url='https://'+server_ip+ redfish['SNMP'], auth=auth, body=redfish['Disable SNMP'])
    if Disable_SNMP[0] == 200:
        print('SNMP disabled')
    else:
        print(f'Failed, Status code: {Disable_SNMP[0]}')

    # 找到Account建立在哪個Link, 針對Link做Delete
    jdata = GET(url='https://'+server_ip+ redfish['Accounts'], auth=auth)[-1].json()
    count = str(jdata['Members@odata.count']+1)
    Delete = DELETE(url='https://'+server_ip+ redfish['Accounts'] + count, auth=auth)
    if Delete[0] == 200:
        print(f'Account ID {count} has deleted')
    else:
        print(f'Failed, Status code: {Delete[0]}')
        exit()

if __name__ == '__main__':
    print(f'Server: {server_ip}')
    Redfish_setup()

    if Get_Only:
        snmpv2_test(server_ip, port, community_key, oid)
        snmpv2_test(server_ip, port, account, v3_key, oid)  
    else:
        snmpv2_test(server_ip, port, community_key, oid, value=uid_on)
        snmpv2_test(server_ip, port, community_key, oid)
        # UID_Change(Change)
        snmpv2_test(server_ip, port, community_key, oid, value=uid_off)
        snmpv2_test(server_ip, port, community_key, oid)

        snmpv3_test(server_ip, port, account, v3_key, oid, value=uid_on)
        snmpv3_test(server_ip, port, account, v3_key, oid)

        snmpv3_test(server_ip, port, account, v3_key, oid, value=uid_off)
        snmpv3_test(server_ip, port, account, v3_key, oid)
        Change = "Off"
        print('Test Disable account')      
        Disable_Account(Account_Enable=False)
        snmpv3_test(server_ip, port, account, v3_key, oid)
    Clear_setup()


    # https://www.jianshu.com/p/739803ca71d5
    # https://blog.csdn.net/OldHusband/article/details/102568620
    # Type SNMPv2 command to get UID status 'snmpget -v2c -c public <BMC_IP> 1.3.6.1.4.1.21317.1.10.0'
    # Type SNMPv3 command to get UID status 'snmpget -v3 -u <user_name> -a MD5 -A "*****" -x DES -X "*****" -l authPriv <BMC_IP> 1.3.6.1.4.1.21317.1.10.0'
    # https://github.com/pyasn1/pyasn1/issues/28  issue using pyasn1-0.5.0 and pysnmp-4.4.12 when I use getcmd().

def v3_test_code():
    oid = ".1.3.6.1.4.1.2021.11.9.0"
    oid_obj = ObjectType(ObjectIdentity(oid))
    combo = 'MD5/DES'
    combo2 = 'SHA1/AES'
    name = combo.replace('/','')
    credentials = UsmUserData(name, authKey='Aa123456')
    
    # UsmUserData 是 pysnmp 中用於配置 SNMPv3 使用者（User）的類別。SNMPv3 是 SNMP 的一個安全版本，它使用使用者名稱（User Name）和相應的認證及加密金鑰來確保 SNMP 的安全性。
    SHA_credentials = UsmUserData(name, authKey='Aa123456', privKey='Aa123456', authProtocol=usmHMACSHAAuthProtocol )
    MD5_credentials = UsmUserData(name, authKey='Aa123456', privKey='Aa123456', authProtocol=usmHMACMD5AuthProtocol )
    AES_credentials = UsmUserData(name, authKey='Aa123456', privKey='Aa123456', privProtocol=usmAesCfb128Protocol )
    DES_credentials = UsmUserData(name, authKey='Aa123456', privKey='Aa123456', privProtocol=usmDESPrivProtocol )

    # getCmd() 函數用於發送單個的 SNMP GET 請求
    # 而 nextCmd() 函數用於發送連續的 SNMP GETNEXT 請求（也稱為 SNMP WALK）