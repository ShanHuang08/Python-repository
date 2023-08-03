from pysnmp.hlapi import *

def snmp_get(server_ip, account, password, oid):
    # 定義 SNMP Community 和 SNMP 版本
    community = CommunityData(account, mpModel=0)

    # 定義目標設備
    target = UdpTransportTarget((server_ip, 161))

    # 定義 SNMP 請求的 OID
    oid_obj = ObjectType(ObjectIdentity(oid))

    # 建立 SNMP GET 請求
    get_request = getCmd(SnmpEngine(), community, target, ContextData(), oid_obj)

    # 執行 SNMP GET 請求
    error_indication, error_status, error_index, var_binds = next(get_request)

    # 處理回應結果
    if error_indication:
        print(f"錯誤: {error_indication}")
    elif error_status:
        print(f"錯誤: {error_status.prettyPrint()} at {error_index and var_binds[int(error_index)-1][0] or '?'}")
    else:
        for var_bind in var_binds:
            # 取得 SNMP 回傳的值
            value = var_bind[-1]
            print(f"OID: {var_bind[0]}, Value: {value}")

if __name__ == '__main__':
    server_ip = '10.10.10.10'
    account = 'Admin'
    password = 'test1234'
    oid = ".1.3.6.1.4.1.2021.11.9.0"

    snmp_get(server_ip, account, password, oid)

    # https://www.jianshu.com/p/739803ca71d5