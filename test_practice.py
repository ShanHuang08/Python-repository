from Library.Call_Method import call
from ssh_connect import ssh_os
from SUT import GetFWInfo

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

def SMC_tools():
    from Library.SMCIPMITool import SMCIPMITool, SMCIPMITool_Internal
    smc, smc_in = SMCIPMITool(ip, uni_pwd), SMCIPMITool_Internal(ip, uni_pwd)
    print(f'Server IP: {ip}')
    return smc, smc_in

if __name__=='__main__':
    ip = '10.184.23.61'
    uni_pwd = 'MKQBSKZCNJ'
    smc, smc_in = SMC_tools()

    # call.Search_FW_Num('', 'H13SVW')
    # smc.raw_30_48_1()
    # smc_in.Check_BS()
    # smc.Raw_Factory_Default()
    # call.Modify_Frus(ip, uni_pwd, 'PN')
    # smc.smc_command('ipmi fruw PS PS241022')
    # smc.raw_30_68_28_00() #Check provision status
    # ssh_os('10.184.12.210', 'X13SEI.txt')s
    # call.Mount_isos(ip, uni_pwd, 1, mount=True)
    # call.StringGenerator(64)
    # call.Set_Pre_Test_Pwd_to_ADMIN(1,2,3,4)
    # GetFWInfo('10.184.17.43', guid=False, OpenBMC=False)