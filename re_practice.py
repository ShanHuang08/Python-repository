import re
from datetime import datetime
from lxml import etree
from scapy.all import AsyncSniffer, send, IP, ICMP, IPv6, ICMPv6EchoRequest
reformat = r"^b'\<([0-9]{1,3})\>([A-Za-z]{3} [0-9 ]{2} \d{2}:\d{2}:\d{2}) ((([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) ([\S\s]+)"

pattern = r'Setting: "<([^>]+)>([^<]+)</\1>"'

# print("C:\\Users\\Username\\Documents")
# print(r"C:\Users\Username\Documents")

Ori_xml = r'D:\Old\H13SRD-F\01.01.05\bmccfg_0712_1558.xml'

TagName = ['child8', 'child9']
TagValue = ['Newtest', 'test9']

bmc_ip = '10.184.16.55'
fake_ip = '127.0.0.1'
def blocked(bmc_ip, fake_ip):
    t = AsyncSniffer(
        iface='eth0', filter=f'src host {bmc_ip} and dst host {fake_ip}')
    t.start()
    send(IP(dst=bmc_ip, src=fake_ip)/ICMP(), count=3, inter=0.5)
    t.stop()
    return True if not t.results else False

blocked(bmc_ip, fake_ip)
# OSError: eth0: No such device exists (No such device exists)
