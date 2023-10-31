import re
from datetime import datetime
from lxml import etree
from Library.Redfish_requests import *
from Library.Strings import StrReverse, StringGenerator


reformat = r"^b'\<([0-9]{1,3})\>([A-Za-z]{3} [0-9 ]{2} \d{2}:\d{2}:\d{2}) ((([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) ([\S\s]+)"

pattern = r'Setting: "<([^>]+)>([^<]+)</\1>"'

# print("C:\\Users\\Username\\Documents")
# print(r"C:\Users\Username\Documents")
import Library.dictionary as dic
dic.RawCommands
Ori_xml = r'D:\Old\H13SRD-F\01.01.05\bmccfg_0712_1558.xml'

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

def OcttoHex():
    Oct = int(input('Input Oct: '))
    return print(hex(Oct)[2:].upper())

path = '/redfish/v1/Managers/1/Oem/Supermicro/NTP'

# enumerate_practice()
# print(int('40', 16))
# print(hex(192)[2:].upper())

def set_ipv6_gateway(gateway:str):
    print(f'30 68 09 02 {gateway}')
# set_ipv6_gateway('test2')


def raw_byte_array():
    value = input('Input 30 68 0A return code: ')
    excepted = input('Input IP address: ')
    value = value.strip()
    Value_NoSpace = ''.join(value.split())
    Transfer_value = bytearray.fromhex(Value_NoSpace).decode()
    if Transfer_value == excepted:
        print(f"Both values match")
    else:
        print(f"{Transfer_value} != {excepted}")
    
raw_byte_array()
# StringGenerator()

