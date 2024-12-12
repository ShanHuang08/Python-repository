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
    smc = SMCIPMITool(ip, uni_pwd)
    print(f'Server IP: {ip}')
    return smc

def smc_in():
    from Library.SMCIPMITool import SMCIPMITool_Internal
    smc_in = SMCIPMITool_Internal(ip, uni_pwd)
    print(f'Server IP: {ip}')
    return smc_in

def _print_method_info(self, method, uri, exp_code=None, header=None, data=None):
    from robot.api import logger
    if exp_code is not None and header is None and data is None:
        logger.info(f"making {method} request on {uri} and expecting status code {exp_code}...")
    elif exp_code is not None and header is not None and data is None:
        logger.info(f"making {method} request on {uri} with header {header} and expecting status code {exp_code}...")
    elif exp_code is not None and header is None and data is not None:
        logger.info(f"making {method} request on {uri} with body {data} and expecting status code {exp_code}...")
    elif exp_code is not None and header is not None and data is not None:
        logger.info(f"making {method} request on {uri} with header {header} and body {data} and expecting status code {exp_code}...")
    elif exp_code is None and header is None and data is None:
        logger.info(f"making {method} request on {uri}...")
    elif exp_code is None and header is not None and data is None:
        logger.info(f"making {method} request on {uri} with header {header}...")
    elif exp_code is None and header is None and data is not None:
        logger.info(f"making {method} request on {uri} with body {data}...")
    elif exp_code is None and header is not None and data is not None:
        logger.info(f"making {method} request on {uri} with header {header} and body {data}...")


def make_get_request(self, uri, user="", pw="", exp_code=None):
    """ This method will make a GET request of the given URI """
    from robot.api import logger
    self._print_method_info("GET", uri, exp_code)
    if len(uri.split('.')) != 4 or "MRVL" in uri or "Base" in uri or "HBA" in uri or "HA-RAID" in uri:
        uri = "https://" + self.ip + uri
    if not user and not pw:
        # Set user/pw if user/pw is not given
        user = self.username
        pw = self.password
    logger.debug(f"using username {user} / password {pw}")
    try:
        resp = self._create_session().get(uri, auth=(user,pw), verify=False, timeout=60)
    except ConnectionError:
        raise RedfishError('Connection lost on request.')
    if exp_code and (resp.status_code != int(exp_code)):
        raise RedfishError(
            "GET request with {}/{} - status code should be {} but it is {}\nResponse body: {}".format(
                user, pw, exp_code, resp.status_code, resp.text))
    return resp


if __name__=='__main__':
    ip = '172.31.34.128'
    uni_pwd = 'labadmin'

    # GetFWInfo('172.31.34.128', guid=False, OpenBMC=False)
    # call.Search_FW_Num('', 'X12dpt-pt')
    # smc().raw_30_48_1()
    # smc_in().Check_BS()
    # smc().Raw_Factory_Default()
    # call.Modify_Frus(ip, uni_pwd, 'BS')
    # smc().smc_command('ipmi fruw PS PS241022')
    # Redfish_setup(ip)
    # ssh_os('10.184.28.199', 'X12DPT-PT.txt')
    # call.Mount_isos(ip, uni_pwd, 1, mount=False)
    # call.StringGenerator(64)
    # call.Set_Pre_Test_Pwd_to_ADMIN(1,2,3,4)