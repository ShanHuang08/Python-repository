# from Library.Redfish_requests import *
from time import sleep
from Redfish_requests import *

ip = '10.184.28.110'
auth = ('ADMIN', 'ADMIN')

def Get_PostCode(ip, auth):
    # 寫個while loop, power state on = False. off = True
    text = ''
    for i in range(40):
        jdata = GET(url='https://'+ip+'/redfish/v1/Managers/1/Oem/Supermicro/Snooping/', auth=auth)[-1]
        print(f"{i+1}. PostCode = {jdata['PostCode']}, {type(jdata['PostCode'])}")
        text = jdata['PostCode']
        # print(text)
        sleep(5)

Get_PostCode(ip, auth)
