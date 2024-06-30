import re, sys
from Library.Call_Method import ASCII_to_raw, StringGenerator, CN_Generator
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

def is_ipv4(ip):
    ipv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'  
    match = re.match(ipv4_pattern, ip)
    if match: 
        Check = [ip.split('.')[i] for i in range(0,4) if 0 <= int(ip.split('.')[i]) <= 255]
        return len(Check) == 4
    else: return False