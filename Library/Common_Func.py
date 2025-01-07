import subprocess
import re
import os
from Library.Redfish_requests import GET
from time import sleep
from Library.Execeptions import SMCError
import requests
from urllib3.exceptions import NewConnectionError
from requests.exceptions import ConnectionError

def Check_ipaddr(ip:str):
    """ping -n 2 ip address or url"""
    if ip.startswith('http'): ip = ip.split('//')[-1]
    if ip.endswith('/'): ip = ip[:-1]
    command = 'ping -n 2 ' + ip
    Ping = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    return True in ['TTL=' in line for line in Ping.stdout.splitlines()]

def Check_ip_is_stable(ip:str, counts=10):
    print(f'Server IP: {ip}')
    if ip.startswith('http'): ip = ip.split('//')[-1]
    if ip.endswith('/'): ip = ip[:-1]
    command = f'ping -n {counts} {ip}' 
    Ping = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    # print(Ping.stdout) #Debug
    success = [line for line in Ping.stdout.splitlines() if 'TTL' in line]
    err = counts - len(success) #10 - 8
    if err == 0: print('SUT ping is stable')
    elif err == counts:
        print(f'{err} packets loss of {counts}\nAll packets are loss')
    else: print(f'SUT is unstable\n{err} packets loss of {counts}')
    return err == 0

def is_ipv4(ip):
    ipv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'  
    match = re.match(ipv4_pattern, ip)
    if match: 
        Check = [ip.split('.')[seg] for seg in range(0,4) if 0 <= int(ip.split('.')[seg]) <= 255]
        return len(Check) == 4
    else: return False

def Check_Pwd_via_Redfish(ip, unique):
    Auth = ('ADMIN', 'ADMIN')
    try:
        Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1', auth=Auth)
        # Can't login to   (Login error message from SMCIPMITool), 用tool會造成互call
        if Check_Network is not None: 
            if Check_Network[0] == 500:
                print(f"GET /redfish/v1/Managers/1 return 500\n GET Systems/1")
                Check_Network = GET(url='https://'+ip+'/redfish/v1/Systems/1', auth=Auth) 

            if isinstance(Check_Network, list):
                    if Check_Network[0] == 200: return Auth
                    # elif Check_Network[0] == 401 and 'error' in Check_Network[1]: #Legacy response包含error, Openbmc只會有Unauthorized
                    else: return ('ADMIN', unique)        
        else:
            print('GET /redfish/v1/Managers/1 return None\nSUT is disconnected')
            # exit()
    except NewConnectionError as err:
        print(f'NewConnectionError: {err}')
    except ConnectionError as err:
        print(f'ConnectionError: {err}')
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


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
        print(f'Ping SUT {ip} failed\nWaiting for 10s')
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
        
def log(content, Debug=bool):
    """Only print() if Debug == `True`"""
    if Debug: print(content)

def is_only_dot(cmd:str):
    special_ch = '!@#$%^&*()_+<>?./:;'
    no_err = True
    for s in special_ch:
        if s in cmd: no_err = False
    return no_err

def RunTime(method, timeout=5):
    """Count method running time"""
    import time
    Start_Time = time.time()
    try:
        method() # method as object, method() as function
        End_Time = time.time()
        elapsed_time = End_Time - Start_Time
        if elapsed_time == 0.000: elapsed_time = 0.001 
        print(f'Elapse {elapsed_time:.3f} secs')
    except Exception as e:
        End_Time = time.time()
        elapsed_time = End_Time - Start_Time
        AssertionError(f'Method execution fail: {e}\nElapse {elapsed_time:.3f} secs')

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