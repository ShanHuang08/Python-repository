from Library.dictionary import *
from Library.SMCIPMITool import SMCIPMITool
from Library.Call_Method import Check_PWD, ASCII_to_raw, Get_Dict, get_lani_id_list, Email_Format, smc_command
from time import sleep

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
    
def Check_Fru1(ip, uni_pwd):
    pwd=Check_PWD(ip, uni_pwd)[1]
    SMC_tool = SMCIPMITool(ip, pwd)
    fru1 = SMC_tool.Execute('ipmi fru1')
    for out in fru1.splitlines():
        if any(j in out for j in ['BPN','BS','BP','BV']):
            print(out)       
# Check_Fru1()

# lani = get_lani_id_list(ip, uni_pwd)
# print(lani)

def tinydict():
    return {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}


text = 'qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwer@qwert.qqq'
# text = 'qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwer@abc.com'
# text = 'qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwer@qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwe.qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwe.qwert1'
# text = 'qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwer@qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwe.qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwe.qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qw'
# text = 'hi-there-yes-you-information-abcdefghijklmnopqrstuvwxyz@please-try-to.send-me-an-email-if-you-can-possibly-begin-to-remember-this-coz.this-is-the-longest-email-address-known-to-man-but-to-be-honest.this-is-such-a-stupidly-long-sub-domain-forever.parco.com'
# Email_Format(text)


def raw_Factory_Default(ip, uni_pwd):
    pwd = Check_PWD(ip, uni_pwd)
    timeout = 150 if ip.split('.')[0] == '10' else 160
    SMC_tool = SMCIPMITool(ip, pwd)
    SMC_tool.raw_30_41()
    sleep(timeout)
    SMC_tool.raw_30_48_1()

if __name__=='__main__':
    ip = '10.184.21.204'
    pwd = Check_PWD(ip, 'NLTAFRJLHJ')[1]
    
    SMCIPMITool(ip, pwd).raw_30_48_1()

    # raw_Factory_Default(ip, uni_pwd)
    # smc_command(ip, uni_pwd, 'ipmi oem summary')
    # StringGenerator(64)
    

