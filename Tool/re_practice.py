import re, sys
# from Library.Call_Method import ASCII_to_raw, StringGenerator, CN_Generator
sys.path.append('C:\\Users\\Stephenhuang\\Python')

reformat = r"^b'\<([0-9]{1,3})\>([A-Za-z]{3} [0-9 ]{2} \d{2}:\d{2}:\d{2}) ((([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) ([\S\s]+)"

pattern = r'Setting: "<([^>]+)>([^<]+)</\1>"'
pattern2 = r'(<[a-zA-Z0-9\(\)\.\|\-+/:\~_ ]+>)'


import re

def RStringCheck():
    regex = r"(\d+(?:.\d+)?(?:[a-zA-Z]|.\w+)?)"
    
    for string in ["123", "3.14", "2.7a", "5.", "1.4b.V3"]:
        match = re.match(regex, string)
        print(f"Input: {string}, Match: {match.group()}") if match else print(f"Input: {string}, Not match")

info = "build date: 2023/01/01 version: 1.0"
# regex = r"[a-c]"

def Check_lan_mode():
    regex = r"\[ ((Failover)|(Shared)|(Dedicated)|(Failover-OnBoard)|(Shared-OnBoard)) \].*"
    string = '[ Failover-OnBoard ]'

    match = re.match(regex, string)
    if match: print(f"Input: {string}, Match: {match.group()}")
    else: 
        print(f"Input: {string}, Not match")

FW_Type = {
    'H122' : {'MBD':['H12CCD-TF', 'H12CCD-F']},
    'H12' : {'MBD':['H12SRD-TF', 'H12SSD-F']},
    
    'H13' : {'MBD':['H13SRD-F']},
    'X13' : {'MBD':['X13SRD-TF']}
}

def Find_Device(devi):
    devi = devi.upper()
    matches = bool
    pattern = r'%s.*' % devi  
    print(pattern)
    for key, value in FW_Type.items():
        for mb in value['MBD']:
            match = re.match(pattern, mb)
            print(match)
            matches = True if match else False
            
        if matches: 
            print(FW_Type[key])
            break
        else: print(f"{key} aren't match")

Find_Device('H12ssd')