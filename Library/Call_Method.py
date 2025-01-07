from random import choice, randint, sample
from Library.Redfish_requests import *
from Library.dictionary import *
from Library.SMCIPMITool import SMCIPMITool, SMCIPMITool_Internal
from Library.Common_Func import Check_PWD, Check_ipaddr
from paramiko import SSHClient, ssh_exception, AutoAddPolicy, AuthenticationException, SSHException
from time import sleep
from SUT_IP import FW_Type

class Call_Methods():
    def __init__(self):
        self.al='abcdefghijklmnopqrstuvwxyz'
        self.digit='1234567890'
        self.al_digit = self.al + self.digit
        self.__hide = 'hided variable'
        self.__passwd = 'Supermicro82265990'
        self.IPMICFG_Path = 'C:\\Users\\Stephenhuang\\Desktop\\Tools\\IPMICFG-Linux.x86_64'

    def hide_check(self):
        """Python cannot call `self.__hide` directly. """
        print(f'self.__hide is {self.__hide}')

    def __hided_method(self):
        """Python cannot call `__hided_method` directly."""
        print(f'self.__hide is {self.__hide}')

    @property
    def read_only(self):
        """Add `@property` will show TypeError: 'NoneType' object is not callable"""
        print('This function is read-only')

    def KeyGenerator(self):
        result=''
        for i in range(2):
            List=[]
            for i in range(3):
                TextList=[
                    choice(self.al.upper())+choice(self.digit)+choice(self.al),
                    choice(self.al)+choice(self.digit)+choice(self.al.upper()),
                    choice(self.digit)+choice(self.al.upper())+choice(self.al)]
                List.append(TextList[randint(0,2)])
            # print(List)
            for j in List:
                result+=j
            result=result+'\n'
        return result

    def AI_Optimize(self):
        result = ''
        for i in range(2):
            sub_result = ''.join([f'{choice(self.al.upper())}{choice(self.digit)}{choice(self.al)}' for k in range(3)])
            result += f'{sub_result}\n'
        return result

    def AI_StringGenerator():
        import string
        Num = 32
        multiple = 1
        while Num > 5*multiple:
            multiple+=1

        result = ''
        for Start in range(multiple):
            if Start % 2 != 0:  # 奇數，產生英文字母
                for _ in range(5): 
                    result += choice(string.digits)
            else:  # 偶數，產生數字
                for _ in range(5):
                    result += choice(string.ascii_lowercase)
        print(result[0:Num])

    def StringGenerator(self, Num):
        """
        Input int or str number
        """
        Start = 1
        result = ''
        Num = int(Num)
        while Num > (5 * Start)-1:    
            if Start %2 != 0:
                # print("Num是英文")  #0-4, 10-14
                for i in range(5):
                    result+=choice(self.al)
            else:
                # print("Num是數字") #5-9, 15-16(沒有符合loop條件)
                for i in range(5):
                    result+=choice(self.digit)
            Start+=1

        if Start %2 != 0:
            # print("Num是英文")
            for i in range(5-((5*Start)-Num)): 
                result+=choice(self.al)
        else:
            # print("Num是數字")
            for i in range(5-((5*Start)-Num)):
                result+=choice(self.digit) 

        # print(f"Start={Start}")
        # print(len(result))
        
        print(result)

    def StrReverse(self, Strin):
        """str[::-1]"""
        return Strin[::-1]

    def get_a_random_ip(self, special=False):
        """Generate valid IP address.
        - special is `True` will return all range of IP.
        - special is `False` will exclude IP for special usage."""
        def is_invalid_ip():
            judge_list = [int(first) == 10, '172' in first and 15 < int(second) < 32, '192' in first and '168' in second,
                          first in ['127'], int(first) > 223]
            return True in judge_list
        def is_valid_ip():
            judge_list = [int(first) != 10, '172' in first and int(second) < 15 and int(second) > 32, 
                          '192' in first and '168' not in second, first not in ['127'], int(first) < 223]
            return True in judge_list
        
        while True:
            Gen_ip = ".".join(str(randint(1, 255)) for _ in range(4))
            first = Gen_ip.split('.')[0]
            second = Gen_ip.split('.')[1]
            if special:   
                if is_invalid_ip(): 
                    if first in ['127']: print(f'Generate Loopback ip')
                    elif int(first) > 223: print(f'Generate Muticast ip')
                    else: print(f'Generate Private ip')
                    return Gen_ip
            elif is_valid_ip(): return Gen_ip              

    def generate_special_char(self):
        return sample(',;&*!(){[}]#%+\'"<>=$|^?', 1)[0]

    def AI_ASCII_to_raw(self, url: str) -> str:
        return ' '.join([f"0x{hex(ord(r))[2:]}" for r in url])

    def ASCII_to_raw(self, url:str):
        print(url)
        ASCII_code = [ord(r) for r in url]
        # result = ' '.join(f'0x{hex(i)[2:]}' for i in ASCII_code)
        result = ' '.join(f'{hex(i)[2:]}' for i in ASCII_code)
        # result = ''
        # for i in ASCII_code:
        #     result+=f"0x{hex(int(i))[2:]}" + ' '   
        print(result)

    def CN_Generator(self, num):
        num = int(num)
        text = ''
        swicher = bool
        for _ in range(num):
            random_al_digit = choice(self.al_digit)
            if random_al_digit in '1234567890':
                digit = random_al_digit
                text+=digit
            else:
                if swicher:
                    text+=random_al_digit.upper()
                    swicher = False
                else:
                    text+=random_al_digit.lower()
                    swicher = True

        print(f'CN={text},CN=Users,DC=ad,DC=satc,DC=com\n{text}') 

    def Email_Format(self, text):
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


    def Get_Dict(self, DictVar, path):
        key_list = path.split('.')
        current = DictVar
        for cp in key_list: 
            if isinstance(current, dict):       
                current = current[cp]
        return current

    def GetPath(self, path):
        key_list = path.split('.')
        current = Path 
        for cp in key_list:
            if isinstance(current, dict):
                current = current[cp]
        return current

    def GetRedfish(self, path):
        key_list = path.split('.')
        current = redfish
        for cp in key_list:
            if isinstance(current, dict):
                current = current[cp]
        return current

    def hex_to_dec(self, digit:str):
        answer = []
        for dec in digit.split(' '):
            answer.append(str(int(dec, 16)))
        result = ' '.join(answer)
        print(result)

    def AI_hex_to_dec(self, hex_str:str):
        answer = ' '.join(str(int(dec, 16)) for dec in hex_str.split(' '))
        print(answer)

    def hex_to_unicode(self, digit:str):
        unicode_list = [chr(int(hexv, 16)) for hexv in digit.split(' ')]
        unicode_str = ''.join(unicode_list)
        print(unicode_str)

    def AI_hex_to_unicode(self, hex_str):
        unicode_str = ''.join(chr(int(hex_v, 16)) for hex_v in hex_str.split(' '))
        print(unicode_str)
        return unicode_str
            
    def ssh_inband(self, osip, ip):
        """
        Utilize `ipmitool` or `IPMICFG` to recover SUT via in-band
        """
        print(f"Server: {osip}")
        mask, gateway = self.ip_filter(ip)
        stdoutput = []
        Tool_used = False
        try:
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())      
            ssh.connect(hostname=osip, username='root', password='111111', port=22)
            for cmd in ['ipmitool', './IPMICFG-Linux.x86_64']:
                stdin, stdout1, stderr = ssh.exec_command(cmd)
                stdoutput += stdout1.readlines()
                stdoutput += stderr.readlines()
                # print(''.join(stdoutput))
                stdstrings = ' '.join(stdoutput)

                if not Tool_used:
                    if 'command not found' not in stdstrings:
                        Tool_used = self.ipmitool_recover(ssh, ip, mask, gateway)
                    elif 'IPMICFG Version' in stdstrings: #改成IPMICFG檔名 in stdstrings
                        Tool_used = self.IPMICFG_recover(ssh, ip, mask, gateway)
                    else: print(f"Doesn't have {cmd} tools")  
                    
            ssh.close()
        except ssh_exception.SSHException as e:
            print(f"SSHException occurred: {str(e)}")
        except ssh_exception.NoValidConnectionsError as e:
            print(f'{str(e)}, SSh port is closed!')
        except TimeoutError as e:
            print(f"Connection timed out: {e}")
        
    def ip_filter(self, ip):
        """
        return corresponding `netmask` and `gateway` IPs according to specific location 
        """
        One_Two = ip.split('.')[0]+'.'+ip.split('.')[1]
        if ip.split('.')[0] == '10':
            mask = '255.255.224.0' if One_Two == '10.184' else '255.255.0.0'
            if One_Two == '10.184':
                gateway = '10.184.7.254'
            elif One_Two == '10.140':
                gateway = '10.140.0.250'
            elif One_Two == '10.135':
                gateway = '10.135.0.253'
            return mask, gateway
        else: 
            return '255.255.0.0', '172.31.0.1'
        
    def ipmitool_recover(self, ssh, ip, mask, gateway):
        """Only for `ssh_inband`"""
        print('Execute ipmitool') # Debug only
        for ssh_cmd in [f'ipmitool lan set 1 ipsrc static', f'ipmitool lan set 1 ipaddr {ip}', f'ipmitool lan set 1 netmask {mask}', 
                        f'ipmitool lan set 1 defgw ipaddr {gateway}', 'ipmitool lan print']:
            stdin, stdout, stderr = ssh.exec_command(ssh_cmd)
            for result in stdout.readlines() + stderr.readlines():
                print(result)
        return True

    def IPMICFG_recover(self, ssh, ip, mask, gateway):
        """Only for `ssh_inband`"""
        print('Execute IPMICFG') #Debug only
        for ssh_cmd in ['./IPMICFG -dhcp off', f'./IPMICFG -m {ip}', f'./IPMICFG -k {mask}', f'./IPMICFG -g {gateway}']:
            stdin, stdout, stderr = ssh.exec_command(ssh_cmd)
            for result in stdout.readlines() + stderr.readlines():
                print(result)
        return True

    def String_Split(self, inputs:str):
        inputs = ' '.join(inputs.lstrip().rstrip().split(' '))
        if ',' in inputs or '.' in inputs:
            inputs = ' '.join(inputs.split(','))
            inputs = ' '.join(inputs.split('.'))
        return [s.lstrip() for s in inputs.split(' ') if s != '']

    def Check_Frus(self, SMC_Tool, Types:list, Values:list):
        fru1= SMC_Tool.Execute('ipmi fru1')
        for Type, value in zip(Types, Values):
            for output in fru1.splitlines():
                if Type in output:
                    Actual_value = output.split('=')[-1].lstrip() # Remove left side space
                    print(f"{Type} output: {Actual_value}")
                    if Actual_value == value: print(f'{Type} value match!')
                    else: print(f'{Type} value mismatch!\nActual value: {Actual_value}\nInput value: {value}')
                        
    def Modify_Frus(self, ip, uni_pwd, input_type):
        """
        `input_type` is str that include comma. ex: aa,bb
        """
        print(f'Server IP: {ip}')
        SMC_Tool = SMCIPMITool_Internal(ip, uni_pwd)
        Types = self.String_Split(input_type)
        Values = [input(f"Input {inp} value: ") for inp in Types]

        for typ, value in zip(Types, Values):
            if value != '':
                output1 = SMC_Tool.Execute(f'ipmi fru1w {typ} {value} {self.__passwd}')
                output = SMC_Tool.Execute(f'ipmi fruw {typ} {value}')
                print(f'Fru1 {typ} modify success') if 'Error' not in output1 else print(f'Fru1 {typ} modify failed\n{output1}')
                print(f'Fru {typ} modify success') if 'Error' not in output else print(f'Fru {typ} modify failed\n{output}')         
            else: print(f'{typ} value is empty!')
        # Check if Fru1 values are match
        self.Check_Frus(SMC_Tool, Types, Values)

    def Find_via_FW_Type(self, types, mbd):
        import re
        types = types.strip().upper()
        mbd = mbd.strip().upper()
        pattern = r'%s.*' % mbd
        possible = []
        try: 
            if isinstance(FW_Type[types], list):
                for dics in FW_Type[types]:
                    # if re.match(pattern, dics['MBDs']):
                    if mbd in dics['MBDs']:
                        print(f"{types}\nFW num: {dics['info'][0]}\n{dics['info'][-1]}")
                    else: 
                        possible.append(f"FW num: {dics['info'][0]}\n{dics['MBDs']}")
                # if mbd not in dics['MBDs']: # dics變數在for loop外面仍然可以使用, 返回最後一個值 (Only Python and JS)
                if len(possible) == len(FW_Type[types]):
                    print(types + '\nPossible FW numbers:\n' +'\n'.join(pos for pos in possible) + '\n' + FW_Type[types][-1]['info'][-1])
            else: print(f"{types}\nFW num: {FW_Type[types]['info'][0]}\n{FW_Type[types]['info'][-1]}")
        except KeyError: print(f"Branch {types} is not found!")

    def Find_via_MBDs(self, mbd):
        import re
        matches = False
        PairList = []
        err_msg = [] #Record error output. Error output won't show up if MBD match on the later loop
        mbd = mbd.strip().upper()
        pattern = r'%s.*' % mbd
        if mbd:
            mbd = mbd.upper()
            for key, value in FW_Type.items():
                if isinstance(value, dict):
                    # print(f"{key}\nvalue['MBDs']={value['MBDs']}") #Debug
                    for mb in value['MBDs']:
                        match = re.match(pattern, mb)
                        # print(match) #Debug
                        if match: 
                            matches = True
                            PairList.append(match) #<re.Match object; span=(0, 9), match='H13SAE-MF'>
                            PairList.append(f"{key}\nFW num: {FW_Type[key]['info'][0]}\n{FW_Type[key]['info'][-1]}\n{FW_Type[key]['MBDs']}")
                    if matches:
                        print(f"{key}\nFW num: {FW_Type[key]['info'][0]}\n{FW_Type[key]['info'][-1]}\n{FW_Type[key]['MBDs']}")
                        matches = False
                    elif not matches and mbd[0:3] == value['MBDs'][0][0:3]:
                        err_msg.append(f"{value['MBDs']}")
                        err_msg.append(f"Can't find {mbd} in {key}")

                elif isinstance(value, list):
                    num = 0
                    for val in value:
                        # print(f"{key}\nnum={num}\nval['MBDs']={val['MBDs']}") #Debug
                        for mb in val['MBDs']:
                            match = re.match(pattern, mb)
                            # print(match) #Debug
                            if match: 
                                matches = True
                                PairList.append(match)
                                PairList.append(f"{key}\nFW num: {FW_Type[key][num]['info'][0]} \
                                                \n{FW_Type[key][num]['info'][-1]}\n{FW_Type[key][num]['MBDs']}")
                            
                        if matches:
                            print(f"{key}\nFW num: {FW_Type[key][num]['info'][0]}\n{FW_Type[key][num]['info'][-1]}\n{FW_Type[key][num]['MBDs']}")
                            matches = False
                        elif not matches and mbd[0:3] == val['MBDs'][0][0:3]:
                            err_msg.append(f"{val['MBDs']}")
                            if num == len(value): 
                                err_msg.append(f"Can't find {mbd} in {key}")
                        # print(f'Num= {num}') #Debug
                        num+=1
            if not PairList: print('\n'.join(err_msg))
            return '\n'.join(str(pair) for pair in PairList)
        else: print('Please input MBD value')    
            
    def Search_FW_Num(self, types, mbd):
        '''- EX: `('d301ms', '')`, `('', 'x13dsf-a')`'''
        return self.Find_via_FW_Type(types, mbd) if types.strip() else self.Find_via_MBDs(mbd)

    def Mount_isos(self, ip, uni_pwd, times:int, mount=True):
        if times not in [1,2,3]:
            print(f"times={times}, times arg range should be 1-3")
            exit()
        if not mount: times = 3
        print(f"Server IP: {ip}")
        Auth = Check_PWD(ip, uni_pwd)
        # print(Auth) #Debug

        VM_url = 'https://' + ip + '/redfish/v1/Managers/1/VirtualMedia/VirtualMedia'
        bade_isos = ["http://10.184.10.1/static/att/iso/RHEL9.4.iso", "http://10.184.10.1/static/att/iso/aio9.iso", "https://10.135.0.253/os/redhat/el9a1/aarch64/rhel-baseos-9.1-aarch64-dvd.iso"] 
        us_isos = ["http://172.29.1.248/static/att/iso/RHEL9.4.iso", "http://172.29.1.248/static/att/iso/aio9.iso", "https://172.29.1.237/iso/efishell.iso"]
        tar_isos = bade_isos if ip.split('.')[0] == '10' else us_isos

        # mount/unmount isos
        for time in range(times):
            num = str(time+1) #1,2,3
            url = VM_url + num 
            if mount:
                print(f'Mounting iso {num}')
                setup = PATCH(url, auth=Auth, body={"Oem":{"Supermicro":{"AcceptSelfSigned":False}},"VerifyCertificate":False})
                sleep(3)
                insert = POST(url=url + '/Actions/VirtualMedia.InsertMedia', auth=Auth, body={"Image": tar_isos[time],"Inserted":mount})
                if setup[0] == 200 and insert[0] in [200, 202]: print(f'mount iso {num} success \
                                                                    \nPATCH:{setup[0]}\nPOST:{insert[0]} \
                                                                    \nTask: https://{ip}{insert[-1]["@odata.id"]}')  
                elif 'resource is in use' in setup[1]: print(f'PATCH:{setup[0]}\nMount failed! iso {num} has been mounted, please unmount first!')
                else: print(f'Mount iso {num} failed\nPATCH:{setup[0]}\n{setup[1]}\nPOST:{insert[0]}\n{insert[1]}')
            else:
                print(f'Unmounting iso {num}')
                check_inserted = GET(url, auth=Auth)
                if check_inserted[0] == 200: #api response dict
                    if check_inserted[-1].json()["Inserted"]:
                        uninsert = PATCH(url, auth=Auth, body={"Inserted":mount})
                        if uninsert[0] in [200, 202]: print(f'Unmount iso {num} success\nPATCH:{uninsert[0]}')
                    else: print(f'VM{num} has been unmounted')
                elif check_inserted[0] == 401: 
                    print(f'Status code: {check_inserted[0]}\nPlease check uniquw password.')
                    break

    def use_sftp_upload_file(self, ssh_func, localpath, remotepath):
        """- Utilize `open_sftp()` to upload file to remote path
        - `return True if upload sucessiful`"""
        import os
        try:
            FileName = os.path.basename(localpath)
            print(f'Unable to execute inband cmd\nUpload {FileName} file')
            sftp = ssh_func.open_sftp()
            sftp.put(localpath, remotepath, confirm=True) #Upload file
            sftp.chmod(remotepath+'/'+FileName, 0o777) #Change file permission
            sftp.close()
            return True
        except SSHException as e:
            print(f'{e}\nOS connection failed!')
        except IOError as e:
            print(f"IOError: {e}")
        except Exception as e:
            print(f'Error: {e}')         

    def Inband_tool_check(self, bmc_ip, os_ip):
        """`BMC IP` ,`os_ip:` OS IP"""
        print(f'OS IP: {os_ip}')
        OS_Auth = ('root', '111111')
        try:
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect(os_ip, 22, OS_Auth[0], OS_Auth[1])

            has_ip = []
            for cmd in ['./IPMICFG-Linux.x86_64 -m', 'ipmitool lan print']:
                stdin, stdout, stderr = ssh.exec_command(cmd)
                response = [res for res in stdout.readlines()]
                # print(response) #Debug
                get_ip = ''.join(res for res in response if bmc_ip in res)
                if get_ip:
                    print(f'Get BMC IP from {cmd}:\n{get_ip}')
                    has_ip.append(get_ip)
                else: print(f'BMC info is not match\n{response}')

            # print(has_ip)
            if not has_ip:
                upload = self.use_sftp_upload_file(ssh_func=ssh, localpath=self.IPMICFG_Path, remotepath='/root')
                print('Upload sucessiful') if upload else print('Upload failed!')
                
                stdin, stdout, stderr = ssh.exec_command('./IPMICFG-Linux.x86_64 -m')
                response = [res for res in stdout.readlines()]
                get_ip = ''.join(res for res in response if bmc_ip in res)
                print(f'Get BMC IP from IPMICFG:\n{get_ip}') if get_ip else print(f'BMC info is not match\n{response}')
            ssh.close()

        except AuthenticationException as e:
            print(f'{e}\nLogin Authentication failed!')
        except SSHException as e:
            print(f'{e}\nOS connection failed!')
        except Exception as e:
            print(f'Error: {e}')

    def Set_Pre_Test_Pwd_to_ADMIN(self, *selections, os_check=False):
        """- Input integers, ex: `1,2,3`
        - 1 : 10.184.21.204
        - 2 : 10.184.17.92
        - 3 : 172.31.51.33"""
        devices = [['10.184.21.204', 'NLTAFRJLHJ', '10.184.12.175'], ['10.184.22.116', 'UEIDSZIHBV', ''], 
                   ['172.31.51.33', 'PHYHDTSXUM', '172.31.42.10'], ['10.184.28.13', 'TSEDWYJMKS', '10.184.17.49']]
        # print(','.join(str(sel) for sel in selections)) #(1,2,3)
        def is_valid_args_num():
            invalid_check = [len(selections) == 0, 0 in selections, len(selections) > len(devices),  
                *[int(num) > len(devices) for num in selections]]
            return True not in invalid_check

        if is_valid_args_num():
            devices = [devices[num-1] for num in selections]
        else:
            devices_num = [num for num in range(1, len(devices)+1)] 
            err = [str(num) for num in selections if num not in devices_num]
            print(f"Invalid values: {','.join(err)} in {selections}")
            exit()

        for info in devices: 
            smc = SMCIPMITool(info[0], info[1])
            if not os_check: info[2] = ''
            if Check_ipaddr(info[0]):
                print(f'Server IP: {info[0]}')

                if Check_ipaddr(info[2]) and info[2]:
                    self.Inband_tool_check(info[0], info[2])
                else: 
                    if info[2]: print(f'{info[2]} connection failed')
                    elif not os_check: print('SUT does not check OS IP')
                    else: print('SUT does not have OS IP')

                passwd = smc.pwd.strip()
                if passwd != 'ADMIN':
                    output = smc.raw_30_48_1()
                    if "Can't connect to" in output: print('SUT RMCP is not responding')
                    elif "Can't login to" in output and '00' not in output: print('Password is ADMIN')
                else: 
                    smc.check_rakp()
                    print(f"Password is {passwd}")
            else: print(f'{info[0]} is offline')

    def check_time_diff(self):
        import time
        def convert_web_time_to_seconds(text):
            time_strt = time.strptime(text, "%Y-%m-%dT%H:%M:%S%z")
            res = time.mktime(time_strt)
            print(time_strt, res)
            print(f'Converted {text} to {res} seconds')
            return res
        des_time = convert_web_time_to_seconds(text='2024-11-11T11:33:45Z')
        cur_time = time.time()
        #  print(cur_time, des_time)
        print(f'Current time subtract destinated time = {int(cur_time) - int(des_time)} secs')

call = Call_Methods()