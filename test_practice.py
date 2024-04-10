from Library.SMCIPMITool import SMCIPMITool
from Library.Call_Method import Check_PWD


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



test = 'a'
def tinydict():
    return {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

# print(isinstance(test, str))
# print(isinstance(test, int))
# print(isinstance(tinydict(), int))
# print(isinstance(tinydict(), dict))

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student:
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree

# print(isinstance(Animal('Lion', 3), Animal))
# print(isinstance(Animal('Lion', 3), Student))
# print(isinstance(Student('Student', '7th'), Student))


def is_number(numb):
    if isinstance(numb, int):
        print(f'變數 {numb} 為int')
    else:
        print(f'變數 {numb} 是 {type(numb)}')

# is_number(7)
# is_number(2.5)
# is_number('7')
# is_number({7})
# is_number({'number' : 7})


def Email_Format():
    text = 'qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwer@qwert.qqq'
    # text = 'qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwer@abc.com'
    # text = 'qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwer@qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwe.qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwe.qwert1'
    # text = 'qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwer@qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwe.qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwe.qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qw'
    # text = 'hi-there-yes-you-information-abcdefghijklmnopqrstuvwxyz@please-try-to.send-me-an-email-if-you-can-possibly-begin-to-remember-this-coz.this-is-the-longest-email-address-known-to-man-but-to-be-honest.this-is-such-a-stupidly-long-sub-domain-forever.parco.com'

    first_text_cut = text.split('@')[0]
    length = text.split('.')
    second_text_cut = text.split('@')[1].split('.')[0] if len(length) > 0 else None
    Third_text_cut = text.split('@')[1].split('.')[1] if len(length) > 1 else None
    forth_text_cut = text.split('@')[1].split('.')[2] if len(length) > 2 else None

    print(f"Local-part: {first_text_cut}") 
    print(f"Local-part length is {len(first_text_cut)}\n") #length == 64 

    if len(length) > 0:
        print(f"Domain 1st label: {second_text_cut}")
        print(f"Domain 1st label length is {len(second_text_cut)}\n") # length == 63
    if len(length) > 1:
        print(f"Domain 2nd label: {Third_text_cut}")
        print(f"Domain 2nd label length is {len(Third_text_cut)}\n") # length == 63
    if len(length) > 2:
        print(f"Domain 3rd label: {forth_text_cut}")
        print(f"Domain 3rd label length is {len(forth_text_cut)}\n") # length == 5

Email_Format()
        
# StringGenerator(64)

