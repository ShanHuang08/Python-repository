import subprocess
import os
from Library.Execeptions import SMCError, SUMError

class SMCIPMITool():
    def __init__(self, ip, pwd) -> None:
        self.Path = 'C:\\Users\\Stephenhuang\\SMCIPMITool_2.28.0_build.231120_bundleJRE_Windows'
        self.ip = ip
        self.pwd = pwd

    def Execute(self, cmd:str):
        if os.path.exists(self.Path):
            execute = subprocess.run('SMCIPMITool.exe '+ self.ip +' ADMIN '+ self.pwd +' '+cmd, shell=True, capture_output=True, universal_newlines=True, cwd=self.Path)
            # print(self.ip, self.pwd, cmd)
            if execute.stderr == '':
                return execute.stdout
            else:
                return execute.stderr
        else:
            print(SMCError())

    def raw(self, cmd:str):
        self.Execute('ipmi raw '+cmd)

    def raw_30_68_09(self, cmd:str):
        self.raw('30 68 09 '+cmd)

    def raw_30_68_0A(self, cmd:str):
        self.raw('30 68 0A '+cmd)

class SUMTool():
    def __init__(self, ip, pwd) -> None:
        self.Path = 'C:\\Users\\Stephenhuang\\sum_2.11.0_Win_x86_64'
        self.ip = ip
        self.pwd = pwd
    
    def Execute(self, cmd:str):
        if os.path.exists(self.Path):
            execute = subprocess.run('sum.exe -i '+self.ip+' '+'-u ADMIN -p '+self.pwd+' -c '+cmd, shell=True, capture_output=True, universal_newlines=True, cwd=self.Path)
            if execute.stderr == '':
                return execute.stdout
            else:
                return execute.stderr
        else:
            print(SUMError())

    def get_bmc_info(self):
        self.Execute('GetBmcInfo')
    
    def get_bios_info(self):
        self.Execute('GetBiosInfo --showall')
    
    def get_cpld_info(self):
        self.Execute('GetCpldInfo')

# SMC_tool = SMCIPMITool()