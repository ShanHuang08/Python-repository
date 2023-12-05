import subprocess
import os
from Library.Execeptions import SMCError

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
                print(execute.stdout)
                return execute.stdout
            else:
                print(execute.stderr)
                return execute.stderr
        else:
            print(SMCError())

    def raw(self, cmd:str):
        self.Execute('ipmi raw '+cmd)

    def set_30_68_09(self, cmd:str):
        self.raw('30 68 09')

    def set_30_68_0A(self, cmd:str):
        self.raw('30 68 0A')

# SMC_tool = SMCIPMITool()