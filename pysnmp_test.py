from pysnmp.hlapi import *
import pyasn1
def snmpv2_get(server_ip, community_key, oid):
    # 定義 SNMP Community 和 SNMP 版本
    community = CommunityData(community_key, mpModel=1)
    # print(f'community= {community}, {type(community)}')
    # community= CommunityData(communityIndex='s6959421844976907261', communityName=<COMMUNITY>, mpModel=1, contextEngineId=None, contextName=b'', tag=b'', securityName='s6959421844976907261'), <class 'pysnmp.hlapi.auth.CommunityData'>
    
    # 定義目標設備
    target = UdpTransportTarget((server_ip, 161))
    # print(target)
    # UdpTransportTarget(('10.184.20.66', 161), timeout=1, retries=5, tagList=b'')
    # 定義 SNMP 請求的 OID
    oid_obj = ObjectType(ObjectIdentity(oid))

    # 建立 SNMP GET 請求
    get_request = getCmd(SnmpEngine(), community, target, ContextData(), oid_obj)
    # print(get_request) 
    # <generator object getCmd at 0x00000204671C1D90>

    # 執行 SNMP GET 請求
    error_indication, error_status, error_index, var_binds = next(get_request)
    print(var_binds)
    # [ObjectType(ObjectIdentity(<ObjectName value object, tagSet <TagSet object, tags 0:0:6>, payload [1.3.6.1.4.1.21317.1.10.0]>), <Integer value object, tagSet <TagSet object, tags 0:0:2>, subtypeSpec <ConstraintsIntersection object, consts <ValueRangeConstraint object, consts -2147483648, 2147483647>>, payload [0]>)]
    # 處理回應結果
    if error_indication:
        print(f"錯誤1: {error_indication}, Please enable SNMP and set-up community!")
    elif error_status:
        print(f"錯誤2: {error_status.prettyPrint()} at {error_index and var_binds[int(error_index)-1][0] or '?'}")
    else:
        for var_bind in var_binds:
            # 取得 SNMP 回傳的值
            value = var_bind[-1]
            print(f'Server: {server_ip}\nOID: {var_bind[0]}, Value: {value}')

if __name__ == '__main__':
    server_ip = '10.184.20.66'
    account = 'UserSnmp'
    community_key='Public'
    oid = "1.3.6.1.4.1.21317.1.10.0"

    snmpv2_get(server_ip, community_key, oid)





    # https://www.jianshu.com/p/739803ca71d5

    # Type SNMPv2 command to get UID status 'snmpget -v2c -c public <BMC_IP> 1.3.6.1.4.1.21317.1.10.0'
    # Type SNMPv3 command to get UID status 'snmpget -v3 -u <user_name> -a MD5 -A "*****" -x DES -X "*****" -l authPriv <BMC_IP> 1.3.6.1.4.1.21317.1.10.0'
    # Where is spec
    # https://github.com/pyasn1/pyasn1/issues/28  issue using pyasn1-0.5.0 and pysnmp-4.4.12 when I use getcmd().

def v2_test_code():
    oid = ".1.3.6.1.4.1.2021.11.9.0"
    oid_obj = ObjectType(ObjectIdentity(oid))
    key='public'
    credentials = CommunityData(key, mpModel=1)
    server_ip = '10.10.10.10'
    port = 161
    context=ContextData()
    nextCmd(SnmpEngine(), credentials, UdpTransportTarget((server_ip, port)), context, oid_obj)
    setCmd(SnmpEngine(), credentials, UdpTransportTarget((server_ip, port)), context, oid_obj)

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
    
    server_ip = '10.10.10.10'
    key='Aa123456'
    port = 161
    context=ContextData()
    if combo2 == 'SHA1/AES':
        credentials = UsmUserData(name, authKey='Aa123456', privKey='Aa123456', authProtocol=usmHMACSHAAuthProtocol , privProtocol=usmAesCfb128Protocol )
    
    # get
    nextCmd(SnmpEngine(), credentials, UdpTransportTarget((server_ip, port)), context, oid_obj)

    # set
    setCmd(SnmpEngine(), credentials, UdpTransportTarget((server_ip, port)), context, oid_obj)


    # getCmd() 函數用於發送單個的 SNMP GET 請求
    # 而 nextCmd() 函數用於發送連續的 SNMP GETNEXT 請求（也稱為 SNMP WALK）