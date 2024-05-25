import subprocess
import os
import re
from Library.Execeptions import SMCError, SUMError
from Library.Redfish_requests import GET
from Library.Common_Func import Check_ipaddr, Check_PWD, is_only_dot
from time import sleep

class SMCIPMITool():
    def __init__(self, ip, uni_pwd) -> None:
        self.Path = 'C:\\Users\\Stephenhuang\\SMCIPMITool_2.28.0_build.240411_bundleJRE_Windows'
        self.ip = ip
        self.accout = ' ADMIN '
        self.pwd = Check_PWD(ip, uni_pwd)[1]
    
    def Execute(self, cmd:str):
        if os.path.exists(self.Path):
            execute = subprocess.run('SMCIPMITool.exe '+ self.ip + self.accout + self.pwd +' '+cmd, shell=True, capture_output=True, universal_newlines=True, cwd=self.Path, timeout=120)
            # print(self.ip, self.pwd, cmd)
            if execute.returncode == 0:
                return execute.stdout
            else:
                return f'{execute.stdout}\nError: {execute.stderr}\nReturn code: {execute.returncode}'
        else:
            print(SMCError(f'{self.Path} is not found'))
            exit()

    def raw(self, cmd:str):
        return self.Execute('ipmi raw '+cmd)
    
    def raw_06_01(self):
        print(self.raw('06 01'))
    
    def raw_30_74_01(self):
        """
        - Check if unique password has been activated
        - 01 activated
        """
        print(f"Execute ipmi raw 30 74 01\n{self.raw('30 74 01')}")
    
    def raw_30_68_09(self, cmd:str):
        return self.raw('30 68 09 '+cmd)

    def raw_30_68_0A(self, cmd:str):
        return self.raw('30 68 0A '+cmd)

    def raw_30_41(self):
        print(f"Execute ipmi raw 30 41\n{self.raw('30 41')}")


    def raw_30_48_1(self):
        print(f"Execute ipmi raw 30 48 1\n{self.raw('30 48 1')}")

    def get_sensors(self):
        print(f"Execute ipmi sensor on {self.ip}\n{self.Execute('ipmi sensor --full')}")

    def Check_sensors_status(self):
        """`0E` or `1E`: No sensor, `0F` or `1F`: has sensor"""
        output = self.raw('30 68 F9')
        print(output)
        return output

    def is_sensor_up(self):
        check = self.Check_sensors_status()
        return True if '0F' in check or '1F' in check else False

    def get_lani_id_list(self):
        lani_output = self.Execute('ipmi oem lani')
        # print(lani_output)
        regex = r"\d"
        result = re.findall(regex, lani_output)
        return result

    def Raw_Factory_Default(self):
        print(f'Server IP: {self.ip}')
        timeout = 150 if self.ip.split('.')[0] == '10' else 160
        self.raw_30_41()
        sleep(timeout)
        self.raw_30_48_1()
        sleep(timeout)
        print('Completed') if Check_ipaddr(self.ip) else print(f"{self.ip} is still offline!")

    def smc_commands(self, cmds:str):
        """- Input: cmd A, cmd B, cmd C"""
        cmds = cmds.strip()
        cmds_list = []
        if is_only_dot(cmds):
            cmds_list = cmds.split(',')
            for i in range(len(cmds_list)):
                cmds_list[i] = cmds_list[i].strip()
            for cmd in cmds_list:
                print(f"Execute {cmd}")
                output = self.Execute(cmd)
                print(output)
        else: print('Commands must be separated by commas (,)')


class SMCIPMITool_Internal():
    def __init__(self, ip, uni_pwd) -> None:
        self.Path = 'D:\\SMCIPMITool_2.27.3_(internal)_build.230727_bundleJRE_Windows'
        self.ip = ip
        self.accout = ' ADMIN '
        self.pwd = Check_PWD(ip, uni_pwd)[1]

    def Execute(self, cmd:str):
        if os.path.exists(self.Path):
            execute = subprocess.run('SMCIPMITool.exe '+ self.ip + self.accout + self.pwd +' '+cmd, shell=True, capture_output=True, universal_newlines=True, cwd=self.Path, timeout=120)
            # print(self.ip, self.pwd, cmd)
            if execute.returncode == 0:
                return execute.stdout
            else:
                return f'{execute.stdout}\nError: {execute.stderr}\nReturn code: {execute.returncode}'
        else:
            print(SMCError(f'{self.Path} is not found'))
            exit()    

    def Check_BS(self):
        print(f'Server IP: {self.ip}')
        fru1 = self.Execute('ipmi fru1')
        for output in fru1.splitlines():
            # if any(fru in output for fru in ['BPN','BS','BP','BV']):
            if 'BS' in output:
                print(output)
                SN_number = output.split('=')[-1]
                if len(SN_number) < 10:
                    text = input('Input BS: ')
                    bs1 = self.Execute('ipmi fru1w BS '+ text + ' Supermicro82265990')
                    bs = self.Execute('ipmi fruw BS ' + text)
                    print(f'Fru1 BS modify success') if 'Error' not in bs1 else print(f'Fru1 BS modify failed')
                    print(f'Fru BS modify success') if 'Error' not in bs else print(f'Fru BS modify failed')
                    bs1_num = [num.split('=') for num in bs1.splitlines() if 'BS' in num]
                    bs_num = [num.split('=') for num in bs.splitlines() if 'BS' in num]
                    print(bs1_num+'\n'+bs_num)
                else: print('BS is match')

            if 'BM' in output:
                if 'Supermicro' != output.split('=')[-1].lstrip():
                    print(f"BM doesn't match\nStart override")
                    bm1 = self.Execute('ipmi fru1w BM Supermicro Supermicro82265990')
                    bm = self.Execute('ipmi fruw BM Supermicro')
                    print(f'Fru1 BM modify success') if 'Error' not in bm1 else print(f'Fru1 BM modify failed')
                    print(f'Fru BM modify success') if 'Error' not in bm else print(f'Fru BM modify failed')
                else: print(f"{output}\nBM is match")



class SUMTool():
    def __init__(self, ip, uni_pwd) -> None:
        self.Path = 'C:\\Users\\Stephenhuang\\sum_2.14.0-p1_Win_x86_64'
        self.ip = ip
        self.pwd = Check_PWD(ip, uni_pwd)[1]
    
    def Execute(self, cmd:str):
        if os.path.exists(self.Path):
            execute = subprocess.run('sum.exe -i '+self.ip+' '+'-u ADMIN -p '+self.pwd+' -c '+cmd, shell=True, capture_output=True, universal_newlines=True, cwd=self.Path)
            if execute.returncode == 0 and execute.stdout != '':
                return execute.stdout
            elif execute.returncode == 0 and execute.stdout == '':
                return execute.stderr
            else:
                return f'{execute.stdout}\n{execute.stderr}\n{execute.returncode}'
        else:
            print(SUMError(f'{self.Path} is not found'))

    def get_bmc_info(self):
        print(self.Execute('GetBmcInfo'))
    
    def get_bios_info(self):
        print(self.Execute('GetBiosInfo --showall'))
    
    def get_cpld_info(self):
        print(self.Execute('GetCpldInfo'))
    
    def get_psu_info(self):
        print(self.Execute('GetPSUInfo'))

    def SUT_info(self):
        bmc = self.get_bmc_info()
        bios = self.get_bios_info()
        cpld = self.get_cpld_info()
        psu = self.get_psu_info()
        return f"{bmc}\n{bios}\n{cpld}\n{psu}"

# SMC_tool = SMCIPMITool()