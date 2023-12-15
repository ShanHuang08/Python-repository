import re
from datetime import datetime
from lxml import etree
from Library.Redfish_requests import *
from Library.Call_Method import StrReverse, StringGenerator


reformat = r"^b'\<([0-9]{1,3})\>([A-Za-z]{3} [0-9 ]{2} \d{2}:\d{2}:\d{2}) ((([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) ([\S\s]+)"

pattern = r'Setting: "<([^>]+)>([^<]+)</\1>"'

import Library.dictionary as dic
dic.RawCommands

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
# print(int('40', 16))

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

def AI_ASCII_to_raw(url: str) -> str:
    return ' '.join([f"0x{hex(ord(r))[2:]}" for r in url])

def ASCII_to_raw(url:str):
    ASCII_code = [ord(r) for r in url]
    result = ' '.join(f'0x{hex(i)[2:]}' for i in ASCII_code)
    # result = ''
    # for i in ASCII_code:
    #     result+=f"0x{hex(int(i))[2:]}" + ' '   
    print(result) 
    return result


from Library.SMCIPMITool import SMCIPMITool
from Library.Call_Method import Check_PWD
ip='10.135.172.111'
pwd=Check_PWD(ip=ip, unique='XFFXGWHUVY')[1]
def Check_Fru1():
    SMC_tool = SMCIPMITool(ip, pwd)
    fru1 = SMC_tool.Execute('ipmi fru1')
    for out in fru1.splitlines():
        if any(j in out for j in ['BPN','BS','BP','BV']):
            print(out)       
# Check_Fru1()
def smc_command():
    SMC_tool = SMCIPMITool(ip, pwd)
    output = SMC_tool.Execute('redfish firmwareInventory info')
    print(output)
smc_command()

