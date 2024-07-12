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


from robot.api.deco import keyword
@keyword('Test 2')
def test2():
    """Put it in def __init__(self):
    用于设置 Robot Framework 在执行关键字时搜索库的顺序。
    """
    BuiltIn().set_library_search_order(
            'MultiActions', 'Users', 'IPMISelenium',
            'SeleniumLibrary'
        )


def SMC_tools():
    smc, smc_in = SMCIPMITool(ip, uni_pwd), SMCIPMITool_Internal(ip, uni_pwd)
    return smc, smc_in

if __name__=='__main__':
    ip = '172.31.51.33'
    uni_pwd = 'PHYHDTSXUM'
    smc, smc_in = SMC_tools()

    # sumT = SUMTool(ip, uni_pwd)
    # Search_FW_Num('5501ms', '')
    # smc.raw_30_48_1()
    # smc.Raw_Factory_Default()
    # smc_in.Check_BS()
    # Modify_Frus(ip, uni_pwd, 'BS, BPN')
    # smc.smc_commands('ipmi fru1, ipmi fru')
    # ASCII_to_raw('1234')
    # Email_Format('UHtapQij@EfPnkRUp.c')
    # ssh_os('10.184.20.125', 'X13SAW-F.txt')
    # Mount_isos(ip, uni_pwd, 1)

