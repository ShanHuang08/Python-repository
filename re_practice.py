import re
from datetime import datetime
from lxml import etree
from Library.Redfish_requests import *
from Library.Strings import StrReverse
# from Library.SUT import GetFWInfo
import json
import requests
reformat = r"^b'\<([0-9]{1,3})\>([A-Za-z]{3} [0-9 ]{2} \d{2}:\d{2}:\d{2}) ((([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) ([\S\s]+)"

pattern = r'Setting: "<([^>]+)>([^<]+)</\1>"'

# print("C:\\Users\\Username\\Documents")
# print(r"C:\Users\Username\Documents")

Ori_xml = r'D:\Old\H13SRD-F\01.01.05\bmccfg_0712_1558.xml'

TagName = ['child8', 'child9']
TagValue = ['Newtest', 'test9']

ip = '10.140.176.153'
path = '/redfish/v1/Managers/1/Oem/Supermicro/NTP'
auth = ('ADMIN', 'ADMIN')
url = 'https://'+ip+path
# data = GET_Data(url=url, auth=auth)[1]


# session = requests.session().get('http://www.google.com').json()

data = requests.get(url=url, auth=auth, verify=False).json()



print(type(data))
print(data)

