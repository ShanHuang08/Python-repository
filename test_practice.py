from Library.dictionary import *
from Library.SMCIPMITool import SMCIPMITool, SUMTool, SMCIPMITool_Internal
from Library.Call_Method import ASCII_to_raw, Get_Dict, Email_Format, hex_to_dec, hex_to_unicode, Modify_Frus, Search_FW_Num, Mount_isos
from ssh_connect import ssh_os
from robot.libraries.BuiltIn import BuiltIn

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


def SMC_tools():
    smc, smc_in = SMCIPMITool(ip, uni_pwd), SMCIPMITool_Internal(ip, uni_pwd)
    return smc, smc_in

if __name__=='__main__':
    ip = '10.184.17.92'
    uni_pwd = '2wsx#EDC'
    smc, smc_in = SMC_tools()

    # sumT = SUMTool(ip, uni_pwd)
    # Search_FW_Num('', 'X12SPA')
    # smc.raw_30_48_1()
    # smc.Raw_Factory_Default()
    # smc_in.Check_BS()
    # Modify_Frus(ip, uni_pwd, 'BP')
    # smc.smc_commands('ipmi fru1, ipmi fru')
    # ASCII_to_raw('1234')
    # Email_Format('UHtapQij@EfPnkRUp.c')
    # ssh_os('10.184.26.72', 'H13SAEMF.txt')
    # Mount_isos(ip, uni_pwd, 1)
    # hex_to_dec('F')

