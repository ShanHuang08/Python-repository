from Library.SMCIPMITool import SMCIPMITool, SUMTool, SMCIPMITool_Internal
from Library.Call_Method import ASCII_to_raw, Get_Dict, Email_Format, hex_to_dec, hex_to_unicode, Modify_Frus, Search_FW_Num, Mount_isos, StringGenerator, Set_Pre_Test_Pwd_to_ADMIN
from ssh_connect import ssh_os
from robot.libraries.BuiltIn import BuiltIn

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


from robot.api.deco import keyword
@keyword('Test 2')
def test2():
    """Put it in def __init__(self):
    用于设置 Robot Framework 在执行关键字时搜索库的顺序。
    """
    BuiltIn().set_library_search_order(
            'MultiActions', 'Users', 'IPMISelenium',
            'SeleniumLibrary'
        )

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
    smc, smc_in = SMCIPMITool(ip, uni_pwd), SMCIPMITool_Internal(ip, uni_pwd)
    return smc, smc_in

if __name__=='__main__':
    ip = '10.184.30.29'
    uni_pwd = 'YGEWQIXCVZ'
    smc, smc_in = SMC_tools()

    # Search_FW_Num('', 'h13sae')
    # smc.raw_30_48_1()
    # smc_in.Check_BS()
    # smc.Raw_Factory_Default()
    # Modify_Frus(ip, uni_pwd, 'PN')
    # smc.smc_command('ipmi fruw PS PS241022')
    # smc.raw_30_68_28_00() #Check provision status
    # ASCII_to_raw('1234')
    # ssh_os('10.184.26.72', 'H13SAE.txt')
    # Mount_isos(ip, uni_pwd, 1, mount=True)
    # StringGenerator(64)
    # Set_Pre_Test_Pwd_to_ADMIN(1,2,3,4)