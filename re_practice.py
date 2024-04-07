import re
from Library.Call_Method import ASCII_to_raw, StringGenerator, CN_Generator


reformat = r"^b'\<([0-9]{1,3})\>([A-Za-z]{3} [0-9 ]{2} \d{2}:\d{2}:\d{2}) ((([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) ([\S\s]+)"

pattern = r'Setting: "<([^>]+)>([^<]+)</\1>"'

import re

def RStringCheck():
    regex = r"(\d+(?:.\d+)?(?:[a-zA-Z]|.\w+)?)"
    
    for string in ["123", "3.14", "2.7a", "5.", "1.4b.V3"]:
        match = re.match(regex, string)
        print(f"Input: {string}, Match: {match.group()}") if match else print(f"Input: {string}, Not match")

info = "build date: 2023/01/01 version: 1.0"
# regex = r"[a-c]"
regex = r"\d+"

result = re.findall(regex, info)
print(result)