import subprocess
import os
import re
from Library.Execeptions import SMCError, SUMError
from Library.Common_Func import Check_ipaddr, Check_PWD
from time import sleep
import requests
from subprocess import CalledProcessError

class SMCIPMITool():
    def __init__(self, ip, uni_pwd) -> None:
        self.Path = 'C:\\Users\\Stephenhuang\\SMCIPMITool_2.28.0_build.240703_bundleJRE_Windows'
        self.ip = ip
        Auth = Check_PWD(ip, uni_pwd)
        self.account = f' {Auth[0]} '
        self.pwd = f'{Auth[1]} '
        self.uni_pwd = f'{uni_pwd} '
        self.Auth = Auth
        self.smc_rakp = f'https://{self.ip}/redfish/v1/Managers/1/Oem/Supermicro/SMCRAKP/'
        # print(Auth)
    
    def Execute(self, cmd:str):
        if self.account is None:
            exit()
        self.check_rakp()
        if os.path.exists(self.Path):
            try:
                execute = subprocess.run('SMCIPMITool.exe '+ self.ip + self.account + self.pwd + cmd, shell=True, capture_output=True, 
                                         universal_newlines=True, cwd=self.Path, timeout=120)
                if execute.returncode == 0:
                    return execute.stdout
                else:
                    return f'{execute.stdout}\nError: {execute.stderr}\nReturn code: {execute.returncode}'
            except CalledProcessError as e:
                print(f'CalledProcessError: {e}')
            except FileNotFoundError as e:
                print(f'FileNotFoundError: {e}\nSuggest to add arg Shell=True in subprocess.run()')
        else:
            print(SMCError(f'{self.Path} is not found'))
            exit()

    def raw(self, cmd:str):
        output = self.Execute('ipmi raw '+cmd)
        # print('SMCIPMITool.exe '+ self.ip + self.accout + self.pwd + 'ipmi raw 6 1') #Debug
        return output
    
    def check_rakp(self):
        """Check SMC RAKP status, if it's enabled, disbale it"""
        try:
            check_smc_rakp = requests.get(url=self.smc_rakp, auth=self.Auth, verify=False, timeout=40).json()["Mode"]
            if 'Enabled' in check_smc_rakp:
                print(f'SMC RAKP is enabled\nDisable it')
                off_rakp = requests.patch(url=self.smc_rakp, auth=self.Auth, json={"Mode": "Disabled"}, verify=False, timeout=30)
                if off_rakp.status_code == 200: print('SMC RAKP id disabled')
                else: print(f'Disable failed\nStatus code: {off_rakp.status_code}\nContent: {off_rakp.text}')
            else: print('SMC RAKP is disabled')
        except KeyError as e:
            print(f'KeyError {e} during RAKP check\nDo nothing')
            return

    def raw_06_01(self):
        """Get Device ID"""
        print(self.raw('06 01'))

    def raw_06_04(self):
        """Get Self Test Results
        - PASS: 55"""
        print(self.raw('06 04'))
    
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
        print(f"Execute ipmi raw 30 41")
        output = self.raw('30 41')
        print(f"{output}\n{self.Auth}") if "Can't login to" in output else print(output)

    def raw_30_48_1(self):
        print(f"Execute ipmi raw 30 48 1")
        output = self.raw('30 48 1')
        if "Can't login to" in output:
            print(f"{output}\nWait for 30s")
            sleep(30)
            output2 = self.raw('30 48 1')
            print(output2)
            return output + output2
        else: print(output)
        return output

    def raw_30_0C(self):
        """Get UID status: `off`: 00, `on`: 01 or 02"""
        print(f"Execute ipmi raw 30 0C")
        output = self.raw('30 0C')
        print(output)
        return output

    def raw_30_0D(self):
        """Enable UID"""
        print(f"Execute ipmi raw 30 0D")
        output = self.raw('30 0D')
        print(output)
        return output

    def raw_30_0E(self):
        """Disable UID"""
        print(f"Execute ipmi raw 30 0E")
        output = self.raw('30 0E')
        print(output)
        return output
    
    def raw_30_68_28_00(self):
        """Check RA Provisioning `ROT only`
        - 00: Not Provisioned
        - 01: Provisioned
        - Execute raw 30 68 28 01 start Provisioning
        """
        print(f"Execute ipmi raw 30 68 28 00")
        output = self.raw('30 68 28 00')
        print(output)
        return output
    
    def raw_30_68_e0_00(self):
        """Check POST complete status
        - 0x00 and 0xFF are preserved
        - 0x01 for POST begin
        - 0xFE for POST end
        """
        print(f"Execute ipmi raw 30 68 e0 00")
        output = self.raw('30 68 e0 00')
        print(output)
        return output     

    def get_sensors(self):
        # print(f"Execute ipmi sensor on {self.ip}\n{self.Execute('ipmi sensor --full')}")
        output = self.Execute('ipmi sensor --full')
        return output


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
        """Execute `30 41` and `30 48 01` respectively"""
        timeout = 140 if self.ip.split('.')[0] == '10' else 150
        # print('SMCIPMITool.exe '+ self.ip + self.accout + self.pwd + 'ipmi raw 30 41') #Debug
        self.raw_30_41()
        sleep(timeout)
        self.pwd = self.uni_pwd
        # print('SMCIPMITool.exe '+ self.ip + self.accout + self.pwd + 'ipmi raw 30 48 1') #Debug
        self.raw_30_48_1()
        sleep(timeout)
        print('Completed') if Check_ipaddr(self.ip) else print(f"{self.ip} is still offline!")

    def smc_command(self, cmd:str): 
        output = self.Execute(cmd)
        print(output)

    def smc_commands(self, cmds:str):
        """- Input: cmd A, cmd B, cmd C"""
        cmds = cmds.strip()
        cmds_list = []

        cmds_list = cmds.split(',')
        for i in range(len(cmds_list)):
            cmds_list[i] = cmds_list[i].strip()
        for cmd in cmds_list:
            print(f"Execute {cmd}")
            output = self.Execute(cmd)
            print(output)

    def is_Snmpuser_exist(self):
        # print('SMCIPMITool.exe '+ self.ip + self.accout + self.pwd + 'user list') #Debug
        output = self.Execute('user list')
        # print('SnmpUser' in output) #Debug
        return 'SnmpUser' in output


class SMCIPMITool_Internal():
    def __init__(self, ip, uni_pwd) -> None:
        self.Path = 'D:\\SMCIPMITool_2.27.3_(internal)_build.230727_bundleJRE_Windows'
        self.ip = ip
        Auth = Check_PWD(ip, uni_pwd)
        self.accout = f' {Auth[0]} '
        self.pwd = f'{Auth[1]} '

    def Execute(self, cmd:str):
        if os.path.exists(self.Path):
            try:
                execute = subprocess.run('SMCIPMITool.exe '+ self.ip + self.accout + self.pwd + cmd, shell=True, capture_output=True, 
                                         universal_newlines=True, cwd=self.Path, timeout=120)
                # print(self.ip, self.pwd, cmd)
                if execute.returncode == 0:
                    return execute.stdout
                else:
                    return f'{execute.stdout}\nError: {execute.stderr}\nReturn code: {execute.returncode}'
            except CalledProcessError as e:
                print(f'CalledProcessError: {e}')
        else:
            print(SMCError(f'{self.Path} is not found'))
            exit()    

    def Check_BS(self):
        fru1 = self.Execute('ipmi fru1')
        if 'Error' in fru1: print(fru1)
        for output in fru1.splitlines():
            # if any(fru in output for fru in ['BPN','BS','BP','BV']):
            if 'BS' in output:
                print(output)
                SN_number = output.split('=')[-1]
                if len(SN_number) < 10:
                    text = input('Input BS: ')
                    bs1 = self.Execute('ipmi fru1w BS '+ text + ' Supermicro82265990')
                    bs = self.Execute('ipmi fruw BS ' + text)
                    print(f'Fru1 BS modify success\nFru1: {bs1}') if 'Error' not in bs1 else print(f'Fru1 BS modify failed')
                    print(f'Fru BS modify success\nFru: {bs}') if 'Error' not in bs else print(f'Fru BS modify failed')
                    # bs1_num = [num.split('=') for num in bs1.splitlines() if 'BS' in num] #[['Board Serial Number (BS)       ', ' WM241S005606']]
                    # bs_num = [num.split('=') for num in bs.splitlines() if 'BS' in num]
                else: print('BS is match')

            if 'BM' in output:
                if 'Supermicro' != output.split('=')[-1].lstrip():
                    print(f"BM doesn't match\nStart override")
                    bm1 = self.Execute('ipmi fru1w BM Supermicro Supermicro82265990')
                    bm = self.Execute('ipmi fruw BM Supermicro')
                    print(f'Fru1 BM modify success') if 'Error' not in bm1 else print(f'Fru1 BM modify failed')
                    print(f'Fru BM modify success') if 'Error' not in bm else print(f'Fru BM modify failed')
                else: print(f"{output}\nBM is match")

    def smc_command(self, cmd:str): 
        if 'fru1w' in cmd:
            output = self.Execute(cmd + ' Supermicro82265990')
        else:
            output = self.Execute(cmd)
        print(output)

    def smc_commands(self, cmds:str):
        """- Input: cmd A, cmd B, cmd C"""
        cmds = cmds.strip()
        cmds_list = []

        cmds_list = cmds.split(',')
        for i in range(len(cmds_list)):
            cmds_list[i] = cmds_list[i].strip()
        for cmd in cmds_list:
            print(f"Execute {cmd}")
            if 'fru1w' in cmd:
                output = self.Execute(cmd + ' Supermicro82265990')
            else:
                output = self.Execute(cmd)
            print(output)



class SUMTool():
    def __init__(self, ip, uni_pwd) -> None:
        self.Path = 'C:\\Users\\Stephenhuang\\sum_2.14.0-p8_Win_x86_64'
        self.ip = ip
        Auth = Check_PWD(ip, uni_pwd)
        self.account = Auth[0]
        self.pwd = Auth[1]
        # print(Auth)
    
    def Execute(self, cmd:str):
        if os.path.exists(self.Path):
            try:
                execute = subprocess.run('sum.exe -i '+self.ip+' -u '+self.account+' -p '+self.pwd+' -c '+cmd, shell=True, 
                                         capture_output=True, universal_newlines=True, cwd=self.Path)
                if execute.returncode == 0 and execute.stdout != '':
                    return execute.stdout
                elif execute.returncode == 0 and execute.stdout == '':
                    return execute.stderr
                else:
                    return f'{execute.stdout}\nError: {execute.stderr}\nReturn code: {execute.returncode}'
            except CalledProcessError as e:
                print(f'CalledProcessError: {e}')
        else:
            print(SUMError(f'{self.Path} is not found'))

    def get_bmc_info(self):
        output = self.Execute('GetBmcInfo --showall')
        print(output)
        return output
        # Error:
        # Return code: 146 可以用來判斷
    
    def print_bios_info(self):
        print(self.Execute('GetBiosInfo --showall'))
    
    def get_bios_info(self):
        output = self.Execute('GetBiosInfo --showall')
        print(output)
        return output
    
    def get_cpld_info(self, log=False):
        output = self.Execute('GetCpldInfo')
        if log: print(output)
        return output
    
    def get_psu_info(self):
        output = self.Execute('GetPSUInfo')
        print(output)
        return output

    def SUT_info(self):
        '''return 3 variables, `bmc`, `bios`, `cpld` '''
        bmc = self.get_bmc_info()
        bios = self.get_bios_info()
        cpld = self.get_cpld_info()
        # psu = self.get_psu_info()
        return bmc, bios, cpld

# SMC_tool = SMCIPMITool()