from Library.Redfish_requests import *
import re
from Library.SMCIPMITool import SUMTool


def AddSUT():
    key = input("SUT: ")
    BMC_IP = input("BMC IP: ")
    OS_IP = input("OS IP: ")
    SUT_info = {key : {"BMC" : BMC_IP, "OS" : OS_IP}}
    print(str(SUT_info)[1:-1])

def is_ipv4(ip):
    ipv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'  
    match = re.match(ipv4_pattern, ip)
    if match: 
        Check = [ip.split('.')[i] for i in range(0,4) if 0 <= int(ip.split('.')[i]) <= 255]
        return len(Check) == 4
    else: return False

def Check_PWD(ip):
    """
    - Utilize `Redfish` checking current password
    - If `GET fail` return `unique password`
    """
    if not is_ipv4(ip):
        print(f"Invalid IPv4 format: {ip}")
        exit()

    Auth = ('ADMIN', 'ADMIN')
    Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1', auth=Auth)
    # if Check_Network == None:
    if isinstance(Check_Network, list):
        if Check_Network[0] == 200: return Auth
        elif Check_Network[0] == 401 and 'error' in Check_Network[1]: #Legacy response包含error, Openbmc只會有Unauthorized
            print('Legacy')
            pwd = input('Input unique password: ')
            if pwd == '':
                print('Password is empty!')
                exit()
            return (Auth[0], pwd)
        else:
            Open_auth = ('root', '0penBmc')
            Check_Network2 = GET(url='https://'+ip+'/redfish/v1/Managers/1', auth=Open_auth)
            if Check_Network2[0] == 200: return Open_auth
            elif Check_Network2[0] == 401 and 'error' not in Check_Network2[1]:
                # print('OpenBMC')
                pwd2 = input('Input unique password: ')
                if pwd2 == '':
                    print('Password is empty!')
                    exit()
                return (Open_auth[0], pwd2)
    else:
        print('SUT is disconnected')
        exit()

def is_OpenBMC(ip:str):
    if not is_ipv4(ip):
        print(f"Invalid IPv4 format: {ip}")
        exit()

    Auth = ('ADMIN', 'ADMIN')
    Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1', auth=Auth)
    if isinstance(Check_Network, list):
        if Check_Network[0] == 200: return False
        elif Check_Network[0] == 401 and 'error' in Check_Network[1]: return False
        else: return True
    else:
        print('SUT is disconnected')
        exit()

def GetGUID(ip, account, pwd):
    Mongo_url = f'https://satc.supermicro.com/api/mongohelper/tools/sut/{ip}/{account}/{pwd}/'
    First_Sector = ip.split()[0]
    if First_Sector == '10':
        Mongo_url += '10.184.0.12'
        Guid = GET(url=Mongo_url, timeout=30)
        return print(Guid[-1].json()['guid']) if Guid[0] == 200 else print(f"Status code: {Guid[0]}\n{Guid[1]}")
    else:
        Mongo_url += '172.31.2.47'
        Guid = GET(url=Mongo_url, timeout=30)
        return Guid[-1].json()['guid'] if Guid[0] == 200 else print(f"Status code: {Guid[0]}\n{Guid[1]}")

def Get_LegacyFWInfo(ip:str):
    auth = Check_PWD(ip)
    # auth = ('admin', '2wsx#EDC')
    print(f"Server IP: {ip}")
    url = 'https://'+ip+'/redfish/v1/UpdateService/FirmwareInventory/'
    BMC_Data = None
    BMC_FW = None
    BIOS_Data = None
    BIOS_FW = None
    has_CPLD = False
    CPLD_Ver = None
    Get_Inventory = GET(url=url, auth=auth)

    try:
        # print(GetGUID(ip, account=auth[0], pwd=auth[1]))
        BMC_Data = GET(url=url+'BMC', auth=auth)
        BIOS_Data = GET(url=url+'BIOS', auth=auth)

        Links = Get_Inventory[-1].json()["Members"] #Check CPLD api
        for link in Links:
            if 'CPLD' in link['@odata.id'] and 'Motherboard' in link['@odata.id']: 
                CPLD_link = link['@odata.id']
                has_CPLD = True
        # if not has_CPLD: print(f"Link list: {Links}") #For Debug only

        CPLD_Data = GET(url='https://'+ip+CPLD_link, auth=auth) if has_CPLD else 'Not support CPLD' 
        # print(BMC_Data['Version'])
        if BMC_Data != None and BIOS_Data != None and CPLD_Data != None:
            BMC_FW = BMC_Data[-1].json()['Oem']['Supermicro']['UniqueFilename']
            BIOS_FW = BIOS_Data[-1].json()['Oem']['Supermicro']['UniqueFilename']
            CPLD_Ver = CPLD_Data if CPLD_Data == 'Not support CPLD' else CPLD_Data[-1].json()['Version']
            print(f"{BMC_FW}\n{BIOS_FW}\n{CPLD_Ver}")
        else:
            print(f"BMC types:{type(BMC_Data)}, BIOS types:{type(BIOS_Data)}, CPLD types:{type(CPLD_Data)}")
                  
    except KeyError as e:
        try:
            print(f"{e}\nBMC Data: {BMC_Data[-1].json()['Oem']}\nBIOS Data: {BIOS_Data[-1].json()['Oem']}\nCPLD Data: {CPLD_Data[-1].json()['Version']}")
        except KeyError as e:
            print(f"{e}\nBMC Data: {BMC_Data[-1].json()}\nBIOS Data: {BIOS_Data[-1].json()}\nCPLD Data: {CPLD_Data[-1].json()['Version']}")
        
def Get_OpenFWInfo(ip):
    print(f"Server IP: {ip}")
    url = 'https://'+ip+'/redfish/v1/UpdateService/FirmwareInventory/'
    has_CPLD = False
    auth = Check_PWD(ip)
    Get_Inventory = GET(url=url, auth=auth)

    guid = GetGUID(ip, account=auth[0], pwd=auth[1])
    print(guid)
    
    BMC_ver_num = GET(url+'BMC', auth=auth)[-1].json()['Version']
    BMC_release_date = GET(url+'BMC', auth=auth)[-1].json()['ReleaseDate']
    year = BMC_release_date[0:4]
    month = BMC_release_date[5:7]
    date = BMC_release_date[8:10]

    sumT = SUMTool(ip, auth[1])
    output = sumT.get_bios_info()
    Bios_name = output.splitlines()[-1]
    Bios_name = Bios_name.split(':')[-1].strip()

    Links = Get_Inventory[-1].json()["Members"] #Check CPLD api
    for link in Links:
        if 'CPLD' in link['@odata.id'] and 'Motherboard' in link['@odata.id']: 
            CPLD_link = link['@odata.id']
            has_CPLD = True
    # if not has_CPLD: print(f"Link list: {Links}") #For Debug only
    CPLD_Data = GET(url='https://'+ip+CPLD_link, auth=auth) if has_CPLD else 'Not support CPLD' 

    #因為目前只有個一個branch
    if 'R12' in guid: print(f"BMC_R12AST2600-6401MS_{year}{month}{date}_{BMC_ver_num}_STDsp.zip\n{Bios_name}\n{CPLD_Data[-1].json()['Version']}")
    elif 'R13' in guid: print(f"BMC_R13AST2600-7401MS_{year}{month}{date}_{BMC_ver_num}_STDsp.zip\n{Bios_name}\n{CPLD_Data[-1].json()['Version']}")
    else: pass


def GetFWInfo(ip:str):
    Get_OpenFWInfo(ip) if is_OpenBMC(ip) else Get_LegacyFWInfo(ip)

if __name__=='__main__':
    # AddSUT()
    # print(GetGUID('10.140.179.173', '0penBmc'))
    GetFWInfo('10.140.170.130')

    # SumT = SUMTool('10.140.179.173', '0penBmc')
    # ouput = SumT.get_bmc_info()
    
    
    # for info in ['10.184.11.104', '10.184.21.204']:
    #     GetFWInfo(info)
    #     print('\n')

# Traceback (most recent call last):
#   File "c:\Users\Stephenhuang\Python\Library\SUT.py", line 1, in <module>
#     from Library.dictionary import SUT
# ModuleNotFoundError: No module named 'Library'