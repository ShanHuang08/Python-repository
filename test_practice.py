from Library.Call_Method import call
from ssh_connect import ssh_os
from SUT import GetFWInfo
from Tool.LDAP_setup import Redfish_setup

TagName = ['child8', 'child9']
TagValue = ['Newtest', 'test9']
def enumerate_practice():
    TestDict = {}
    for index, value in enumerate(TagName):
        print(index, value)
        TestDict[index] = value
        if index == len(TagName)-1:
            print(type(index), type(value))
            # <class 'int'> <class 'str'>
    print(TestDict)
# enumerate_practice()

def upload_certificate():
    import requests, json
    from Library.dictionary import redfish
    boot_certs = redfish["CertificateString"]
    # print(boot_certs[1])
    url = 'https://'+ip+'/redfish/v1/Systems/1/Boot/Certificates/'
    payload = {"CertificateString": boot_certs[0], "CertificateType": "PEM"}
    res = requests.post(url, data=json.dumps(payload), auth=('ADMIN', 'ADMIN'), verify=False)
    print(f"Status Code: {res.status_code}\nResponse JSON: {json.dumps(res.json(), indent=4)}\nHeaders: {res.headers}")

def smc():
    from Library.SMCIPMITool import SMCIPMITool
    smc = SMCIPMITool(ip, uni_pwd, rakp=False)
    print(f'Server IP: {ip}')
    return smc

def smc_in():
    from Library.SMCIPMITool import SMCIPMITool_Internal
    smc_in = SMCIPMITool_Internal(ip, uni_pwd)
    print(f'Server IP: {ip}')
    return smc_in

def try_except_else():
    try:
        print('A')
        answer = 1+2
    except Exception as e:
        raise AssertionError(f'Run B\nError: {e}')
    else:
        print('C')

if __name__=='__main__':
    ip = '10.184.29.185'
    uni_pwd = 'YURQEROTVY'

    # GetFWInfo('10.184.22.116', guid=False, OpenBMC=False)
    # call.Search_FW_Num('', 'X13dai')
    # smc().raw_30_48_1()
    # smc_in().Check_BS()
    # smc().Raw_Factory_Default()
    # call.Modify_Frus(ip, uni_pwd, 'BS')
    # smc().smc_command('ipmi fruw PS PS241022')
    # Redfish_setup(ip)
    # ssh_os('10.184.14.2', 'X14DBI.txt')
    # call.Mount_isos(ip, uni_pwd, 1, mount=True)
    # call.StringGenerator(64)
    # call.Set_Pre_Test_Pwd_to_ADMIN(1,2,3,4)
    try_except_else()