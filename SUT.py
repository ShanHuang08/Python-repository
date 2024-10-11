from Library.Redfish_requests import *
import re
from Library.SMCIPMITool import SUMTool
import subprocess, os
from Library.Common_Func import SMCIPMITool

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

def Check_ipaddr(ip):
    command = 'ping -n 1 ' + ip
    Ping = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    List = Ping.stdout.splitlines()
    Text =''.join(line for line in List if "TTL=" in line)
    return len(Text) > 0




def Check_PWD(ip, Open):
    """
    - Utilize `SMCIPMITool` checking current password
    - If `Login fail` require to input `unique password`
    """
    if Open: Auth = ('root', '0penBmc')
    else: Auth = ('ADMIN', 'ADMIN')

    smci = SMCIPMITool(ip, Auth)
    if not is_ipv4(ip):
        print(f"Invalid IPv4 format: {ip}")
        exit()

    Check_Network = smci.raw('6 1')
    if Check_ipaddr(ip):
        # print(Check_Network) #Debug
        if "00" in Check_Network: return Auth
        elif "Can't connect to" in Check_Network: 
            print(f'SUT is disconnected\n{Check_Network}')
            exit()
        elif "Can't login to" in Check_Network:
            uni_pwd = input('Unique Password: ')
            return (Auth[0], uni_pwd)
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

def Get_LegacyFWInfo(ip:str, guid:bool, Open):
    print(f"Server IP: {ip}")
    ip = ip.strip()
    auth = Check_PWD(ip, Open)
    # auth = ('admin', '2wsx#EDC')
    url = 'https://'+ip+'/redfish/v1/UpdateService/FirmwareInventory/'
    BMC_Data = None
    BMC_FW = None
    BIOS_Data = None
    BIOS_FW = None
    has_CPLD = False
    Get_Inventory = GET(url=url, auth=auth)
    CPLD_link = str
    CPLD_Data = str

    try:
        if guid:
            print(GetGUID(ip, account=auth[0], pwd=auth[1]))
        BMC_Data = GET(url=url+'BMC', auth=auth)
        if BMC_Data[0] != 200: 
            print(f"Status code:{BMC_Data[0]}\nSUT api has not responsding\n{BMC_Data[1]}")
            exit()
        BIOS_Data = GET(url=url+'BIOS', auth=auth)
        
        Links = Get_Inventory[-1].json()["Members"] #Check CPLD api
        for link in Links:
            if 'CPLD' in link['@odata.id'] and 'Motherboard' in link['@odata.id']: 
                CPLD_link ='https://'+ip+link['@odata.id']
                # print(CPLD_link) #Debug
                has_CPLD = True
        # if not has_CPLD: print(f"Link list: {Links}") #For Debug only
        if not has_CPLD:
            sumT = SUMTool(ip, auth[1])
            output = sumT.get_cpld_info()
            if 'not supported' in output: CPLD_Data = 'Not support CPLD'
            else:
                for res in output.splitline():
                    if 'CPLD' in res:
                        CPLD_Data = res
        else: CPLD_Data = GET(url=CPLD_link, auth=auth)[-1].json()['Version']

        # print(BMC_Data['Version')
        if BMC_Data != None and BIOS_Data != None and CPLD_Data != None:
            # BMC_Ver = BMC_Data[-1].json()['Version']
            BMC_FW = BMC_Data[-1].json()['Oem']['Supermicro']['UniqueFilename']
            BIOS_FW = BIOS_Data[-1].json()['Oem']['Supermicro']['UniqueFilename']
            # print(f"{BMC_Ver}\n{BMC_FW}\n{BIOS_FW}\n{CPLD_Data}")
            print(f"{BMC_FW}\n{BIOS_FW}\n{CPLD_Data}")
        else:
            print(f"BMC types: {type(BMC_Data)}, BIOS types:{type(BIOS_Data)}, CPLD types:{type(CPLD_Data)}")
                  
    except KeyError as e:
        try:
            print(f"{e}\nBMC Data: {BMC_Data[-1].json()['Oem']}\nBIOS Data: {BIOS_Data[-1].json()['Oem']}\nCPLD Data: {CPLD_Data}")
        except KeyError as e:
            print(f"{e}\nBMC Data: {BMC_Data[-1].json()}\nBIOS Data: {BIOS_Data[-1].json()}\nCPLD Data: {Get_Inventory[-1].json()}")
        
def Get_OpenFWInfo(ip, Open):
    print(f"Server IP: {ip}")
    url = 'https://'+ip+'/redfish/v1/UpdateService/FirmwareInventory/'
    has_CPLD = False
    auth = Check_PWD(ip, Open)
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

    CPLD_Data = str
    Links = Get_Inventory[-1].json()["Members"] #Check CPLD api
    for link in Links:
        if 'CPLD' in link['@odata.id'] and 'Motherboard' in link['@odata.id']: 
            CPLD_link = link['@odata.id']
            has_CPLD = True
    # if not has_CPLD: print(f"Link list: {Links}") #For Debug only
    if not has_CPLD: 
        output = sumT.get_cpld_info()
        if 'not supported' in output: CPLD_Data = 'Not support CPLD'
        else:
            for res in output.splitline():
                if 'CPLD' in res:
                    CPLD_Data = res
    else:
        CPLD_Data = GET(url='https://'+ip+CPLD_link, auth=auth) if has_CPLD else 'Not support CPLD'

    #因為目前只有個一個branch
    if 'R12' in guid: print(f"BMC_R12AST2600-6401MS_{year}{month}{date}_{BMC_ver_num}_STDsp.zip\n{Bios_name}\n{CPLD_Data[-1].json()['Version']}")
    elif 'R13' in guid: print(f"BMC_R13AST2600-7401MS_{year}{month}{date}_{BMC_ver_num}_STDsp.zip\n{Bios_name}\n{CPLD_Data[-1].json()['Version']}")
    # elif 'Xinan_AST2600_OpenBMC' in guid: print(f"BMC_H13AST2600-C501MS_{year}{month}{date}_{BMC_ver_num}_STDsp.zip\n{Bios_name}\n{CPLD_Data[-1].json()['Version']}")
    else: print(f"BMC_H13AST2600-C501MS_{year}{month}{date}_{BMC_ver_num}_STDsp.zip\n{Bios_name}\n{CPLD_Data[-1].json()['Version']}")


def GetFWInfo(ip:str, guid:bool, OpenBMC=False):
    Get_OpenFWInfo(ip, OpenBMC) if OpenBMC else Get_LegacyFWInfo(ip, guid, OpenBMC)

if __name__=='__main__':
    # AddSUT()
    # print(GetGUID('10.140.175.132', 'ADMIN', ''))
    GetFWInfo('10.184.30.66', guid=False, OpenBMC=False)
    

    # SumT = SUMTool('10.140.179.173', '0penBmc')
    # ouput = SumT.get_bmc_info()
    
    
    # for info in ['10.184.21.204', '10.184.17.92', '172.31.51.33']:
    #     GetFWInfo(info, guid=False, OpenBMC=False)
    #     print('\n')

   

# Traceback (most recent call last):
#   File "c:\Users\Stephenhuang\Python\Library\SUT.py", line 1, in <module>
#     from Library.dictionary import SUT
# ModuleNotFoundError: No module named 'Library'