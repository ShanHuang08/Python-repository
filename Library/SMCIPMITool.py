import subprocess
import os
from Library.Execeptions import SMCError, SUMError

class SMCIPMITool():
    def __init__(self, ip, pwd) -> None:
        self.Path = 'C:\\Users\\Stephenhuang\\SMCIPMITool_2.28.0_build.240411_bundleJRE_Windows'
        self.ip = ip
        self.accout = ' ADMIN '
        self.pwd = pwd

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

class SMCIPMITool_Internal():
    def __init__(self, ip, pwd) -> None:
        self.Path = 'D:\\SMCIPMITool_2.27.3_(internal)_build.230727_bundleJRE_Windows'
        self.ip = ip
        self.accout = ' ADMIN '
        self.pwd = pwd

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


class SUMTool():
    def __init__(self, ip, pwd) -> None:
        self.Path = 'C:\\Users\\Stephenhuang\\sum_2.14.0-p1_Win_x86_64'
        self.ip = ip
        self.pwd = pwd
    
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