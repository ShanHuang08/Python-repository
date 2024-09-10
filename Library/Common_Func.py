import subprocess
import re
import os
from Library.Redfish_requests import GET
from time import sleep
from Library.Execeptions import SMCError

def Check_ipaddr(ip):
    command = 'ping -n 1 ' + ip
    Ping = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    List = Ping.stdout.splitlines()
    Text =''.join(line for line in List if "TTL=" in line)
    return len(Text) > 0

def is_ipv4(ip):
    ipv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'  
    match = re.match(ipv4_pattern, ip)
    if match: 
        Check = [ip.split('.')[i] for i in range(0,4) if 0 <= int(ip.split('.')[i]) <= 255]
        return len(Check) == 4
    else: return False

def Check_Pwd_via_Redfish(ip, unique):
    Auth = ('ADMIN', 'ADMIN')
    Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1', auth=Auth)
    # Can't login to   (Login error message from SMCIPMITool), 用tool會造成互cal
    if Check_Network[0] == 500:
        print(f"GET /redfish/v1/Managers/1 return 500\n GET Systems/1")
        Check_Network = GET(url='https://'+ip+'/redfish/v1/Systems/1', auth=Auth) 

    if isinstance(Check_Network, list):
            if Check_Network[0] == 200: return Auth
            # elif Check_Network[0] == 401 and 'error' in Check_Network[1]: #Legacy response包含error, Openbmc只會有Unauthorized
            else: return ('ADMIN', unique)        
    else:
        print('SUT is disconnected')
        exit()


def Check_PWD(ip, unique):
    """
    - Utilize `Redfish` checking current password
    - If `GET fail` return `unique password`
    """
    if not is_ipv4(ip):
        print(f"Invalid IPv4 format: {ip}")
        exit()

    if Check_ipaddr(ip):
        return Check_Pwd_via_Redfish(ip, unique)
    else: 
        print('Ping SUT failed\nWaiting for 10s')
        sleep(10)
        if Check_ipaddr(ip):
            return Check_Pwd_via_Redfish(ip, unique)
        else:
            print('Ping SUT failed\nWaiting for 20s')
            sleep(20)
        if Check_ipaddr(ip):
            return Check_Pwd_via_Redfish(ip, unique)  
        else: 
            print('Ping SUT failed!')
            exit()
        

def is_only_dot(cmd:str):
    special_ch = '!@#$%^&*()_+<>?./:;'
    no_err = True
    for s in special_ch:
        if s in cmd: no_err = False
    return no_err

class SMCIPMITool():
    def __init__(self, ip, Auth) -> None:
        self.Path = 'C:\\Users\\Stephenhuang\\SMCIPMITool_2.28.0_build.240703_bundleJRE_Windows'
        self.ip = ip
        self.accout = f' {Auth[0]} '
        self.pwd = f'{Auth[1]} '
        self.Auth = Auth
        # print(Auth)
    
    def Execute(self, cmd:str):
        if os.path.exists(self.Path):
            execute = subprocess.run('SMCIPMITool.exe '+ self.ip + self.accout + self.pwd + cmd, shell=True, capture_output=True, universal_newlines=True, cwd=self.Path, timeout=120)
            if execute.returncode == 0:
                return execute.stdout
            else:
                return f'{execute.stdout}\nError: {execute.stderr}\nReturn code: {execute.returncode}'
        else:
            print(SMCError(f'{self.Path} is not found'))
            exit()

    def raw(self, cmd:str):
        output = self.Execute('ipmi raw '+cmd)
        # print('SMCIPMITool.exe '+ self.ip + self.accout + self.pwd + 'ipmi raw 6 1') #Debug
        return output