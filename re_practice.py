import re
from datetime import datetime
from lxml import etree
from Library.Redfish_requests import *
from Library.Call_Method import ASCII_to_raw, StringGenerator, CN_Generator


reformat = r"^b'\<([0-9]{1,3})\>([A-Za-z]{3} [0-9 ]{2} \d{2}:\d{2}:\d{2}) ((([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) ([\S\s]+)"

pattern = r'Setting: "<([^>]+)>([^<]+)</\1>"'

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

from Library.SMCIPMITool import SMCIPMITool
from Library.Call_Method import Check_PWD
ip='10.184.28.38'
pwd='WCTFDPTATX'
def Check_Fru1():
    pwd=Check_PWD(ip=ip, unique=pwd)[1]
    SMC_tool = SMCIPMITool(ip, pwd)
    fru1 = SMC_tool.Execute('ipmi fru1')
    for out in fru1.splitlines():
        if any(j in out for j in ['BPN','BS','BP','BV']):
            print(out)       
# Check_Fru1()
def smc_command():
    pwd=Check_PWD(ip=ip, unique=pwd)[1]
    SMC_tool = SMCIPMITool(ip, pwd)
    output = SMC_tool.Execute('Redfish firmwareInventory install')
    print(output)
# smc_command()



# testapi = PATCH(url=url, auth=('user01', 'Suser123'), body="{{test}}")
# print(testapi[0])

# Traceback (most recent call last):
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\models.py", line 971, in json
#     return complexjson.loads(self.text, **kwargs)
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\json\__init__.py", line 346, in loads
#     return _default_decoder.decode(s)
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\json\decoder.py", line 337, in decode
#     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
# json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

# During handling of the above exception, another exception occurred:

CN_Generator(10)

if isinstance():
    pass
