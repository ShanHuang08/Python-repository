from Library.Call_Method import Check_PWD
from Library.SMCIPMITool import SMCIPMITool
from time import sleep

def timeout(ip):
    return 150 if ip.split('.')[0] == '10' else 160

def Check_Mel():
    response = SMC_Tool.Execute('mel list 10')
    Pass_Check = ['PASS' for i in response.splitlines() if 'MEL-0056' in i]
    return len(Pass_Check) > 0

def FactoryDefault(ip):
    commands = ['30 40', '30 41', '30 42', '30 48 0', 'ipmi fd 1', '30 48 1', 'ipmi fd 2', 'ipmi fd 3']
    for cmd in commands:
        if 'ipmi' in cmd:
            SMC_Tool.Execute(cmd)
        else:
            SMC_Tool.raw(cmd)
        sleep(timeout())
        print('MEL-0056 has found\nPASS') if Check_Mel() else print('FAIL')

if __name__=='__main__':
    ip = '10.184.30.32'
    pwd = Check_PWD(ip=ip, unique='test')[1]  
    SMC_Tool = SMCIPMITool(ip=ip, pwd=pwd)
    FactoryDefault(ip)