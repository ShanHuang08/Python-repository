import subprocess
from Library.Redfish_requests import GET, POST, PATCH
from time import sleep
from sys import exit
import requests
import unittest

def Check_SUT():
    Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1/EthernetInterfaces/1', auth=('ADMIN', 'ADMIN'))
    if Check_Network[0] == 200:
        return ('ADMIN', 'ADMIN')
    else:
        pwd = input('Input unique password: ')
        return ('ADMIN', pwd)

def Check_LAN_Interface(ip, auth):
    body = {"Oem" : {"Supermicro" : {"LANInterface" : "Failover"}}}
    Check_Network = GET(url='https://'+ip+'/redfish/v1/Managers/1/EthernetInterfaces/1', auth=auth)
    if Check_Network[-1]['Oem']['Supermicro']['LANInterface'] != 'Failover':
        Change_interface = PATCH(url='https://'+ip+'/redfish/v1/Managers/1/EthernetInterfaces/1', auth=auth, body=body)
        if Change_interface[0] != 200:
            print(Change_interface[1])
            exit()

def BMC_loop(ip, auth):
    count = 0
    try:
        print('Start executing BMC reset cycle')
        for i in range(50):
            POST(url='https://'+ip+'/redfish/v1/Managers/1/Actions/Manager.Reset', auth=auth)
            sleep(150) 
            count+=1
        print(f'Loop done, Execute {count} times')
    except requests.exceptions.ConnectionError as e:
        print(str(e)+'\n'+'Execute'+str(count)+'times')

def Check_ipaddr(ip):
    command = 'ping -n 1 ' + ip
    Ping = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    List = Ping.stdout.splitlines()
    Text=''
    for line in List:
        if "TTL=" in line:
            Text+=line
    return len(Text) > 0

class BMCResetTest(unittest.TestCase):
    def test(self):
        Check_LAN_Interface(ip, auth)
        BMC_loop(ip, auth)  
        if Check_ipaddr(ip):
            print(f'Ping {ip} success')
        else:
            print(f'Ping {ip} failed')

if __name__=='__main__':
    ip = '10.184.28.110'
    auth = Check_SUT()
    unittest.main()

