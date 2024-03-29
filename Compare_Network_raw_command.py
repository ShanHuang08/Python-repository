from Library.dictionary import RawCommands
from Library.SMCIPMITool import SMCIPMITool
from Library.Call_Method import Check_PWD
import subprocess

server_ip = input('Input SUT ip: ')
zA_get = RawCommands['30 68 0A']['Get']
zA_set = RawCommands['30 68 0A']['Set']
z9_get = RawCommands['30 68 09']['Get']
z9_set = RawCommands['30 68 09']['Set']



def prefix(num):
    return hex(num)[2:]

def set_ipv6_data(dhcp_mode:str, auto_config:str, ipv6_opation:str, address:str, prefix:str):
    # 會放在for loop裡面, 要跟dic list對得上
    result = subprocess.run()
    result.stdout
    print((f'30 68 09 01 {dhcp_mode} {auto_config} {ipv6_opation} {address} {prefix}'))

def set_ipv6_gateway(gateway:str):
    result = subprocess.run()
    print(f'30 68 09 {z9_set["Gateway"]} {gateway}')

def get_ipv6_data(data:str):
    result = subprocess.run()
    print(f'30 68 09 00 {data}')
    pass

def test_smcipmitool_30_68_09_set():
    # DHCPv6 Modes + Auto Config
    for mode in [('00', '00', 'STATELESS'), ('00', '01', 'STATELESS'), ('01', '01', 'STATEFUL'), ('02', '00', 'STATIC')]:
        dhcp_mode = mode[0]
        auto_config = mode[1]
        dhcp_mode_str = mode[2]

    # Add IPv6 Address
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 09 01 02 00 00 20 11 00 00 00 00 00 00 00 00 00 00 00 00 11 11 40"
    add_address = '20 11 00 00 00 00 00 00 00 00 00 00 00 00 11 11'
    set_ipv6_data('02', '00', '00', add_address, '40')
    expected_address = '2011::1111'
    # Check ip Address in smcipmitool or redfish
    # making GET request on /redfish/v1/Managers/1/EthernetInterfaces/1/

    # Add Invalid IPv6 Address
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 09 01 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 40"
    add_invalid_address = '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01'
    set_ipv6_data('02', '00', '00', add_invalid_address, '40')
    invalid_address = '::1'
    # Check ip Address in smcipmitool or redfish
    # making GET request on /redfish/v1/Managers/1/EthernetInterfaces/1/

    # Delete IPv6 Address
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 09 01 02 00 01 20 11 00 00 00 00 00 00 00 00 00 00 00 00 11 11 40"
    #test
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 09 01 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    set_ipv6_data('02', '00', '01', add_address, '40')
    # Check ip Address in smcipmitool or redfish
    # making GET request on /redfish/v1/Managers/1/EthernetInterfaces/1/

    # Set Gateway
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 09 02 20 11 00 00 00 00 00 00 00 00 00 00 00 00 11 12"
    set_ipv6_gateway(add_address)
    # Check ip Address in smcipmitool or redfish
    # making GET request on /redfish/v1/Managers/1/EthernetInterfaces/1/

    # Set invalid gateway
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 09 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01"
    set_ipv6_gateway(add_invalid_address)
    # Check ip Address in smcipmitool or redfish
    # making GET request on /redfish/v1/Managers/1/EthernetInterfaces/1/

    # Set duplicate IPv6 address + gateway and reverse
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 09 01 02 00 00 20 11 00 00 00 00 00 00 00 00 00 00 00 00 11 11 40"
    set_ipv6_data('02', '00', '00', add_address, '40') #True
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 09 02 20 11 00 00 00 00 00 00 00 00 00 00 00 00 11 11"
    set_ipv6_gateway(add_address) #False

    #Clear data (use redfish)

    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 09 02 20 11 00 00 00 00 00 00 00 00 00 00 00 00 11 11"
    set_ipv6_gateway(add_address) #False
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 09 01 02 00 00 20 11 00 00 00 00 00 00 00 00 00 00 00 00 11 11 40"
    set_ipv6_data('02', '00', '00', add_address, '40') #True

def test_smcipmitool_30_68_09_get():
    dhcp_mode = get_ipv6_data('00')
    auto_config = get_ipv6_data('01')
    address_list_str = get_ipv6_data('02')
    duid_value = get_ipv6_data('03')
    gateway = get_ipv6_data('04')

def test_smcipmitool_30_68_0a_set():
    # Add dns addresss
    ('ipv4')
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 01 00 00 00 00 00 00" #0.0.0.0 DNS1
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 01 00 00 FF FF FF FF" #255.255.255.255 DNS1
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 01 00 00 0A 02 01 CE" #10.2.1.206 DNS1
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 03 00 00 00 00 00 00" #0.0.0.0 DNS2
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 03 00 00 FF FF FF FF" #255.255.255.255 DNS2
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 03 00 00 0A 02 01 CE" #10.2.1.206 DNS1
    ('ipv6')
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02" #::2 DNS1
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 01 01 00 FE FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF" #feff:ffff:ffff:ffff:ffff:ffff:ffff:ffff DNS1
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 01 01 00 20 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01" #2000::1 DNS1
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00" #:: DNS1
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01" #::1 DNS1
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 01 01 00 FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00" #ff00:: DNS1
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 01 01 00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF" #ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff DNS1
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 01 01 00 FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01" #ff00::1 DNS1
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 03 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02" #::2 DNS2 BMC會reset(HW1)
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 03 01 00 FE FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF" #feff:ffff:ffff:ffff:ffff:ffff:ffff:ffff DNS2
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 03 01 00 20 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01" #2000::1 DNS2 BMC會reset
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 03 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00" #(Invalid data field in Request) DNS2 
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 03 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01" #(Invalid data field in Request) DNS2 
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 03 01 00 FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00" #(Invalid data field in Request) DNS2 
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 03 01 00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF" #(Invalid data field in Request) DNS2
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 03 01 00 FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01" #(Invalid data field in Request) DNS2    
    
    #Del DNS address
    ('ipv6')
    f"SMCIPMITool.exe 1.2.3.4 ADMIN ADMIN ipmi raw 30 68 0A 03 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 04" #hex_address = '0A 02 01 CE'
    f"SMCIPMITool.exe 1.2.3.4 ADMIN ADMIN ipmi raw 30 68 0A 01 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03"
    ('ipv4')
    f"SMCIPMITool.exe 1.2.3.4 ADMIN ADMIN ipmi raw 30 68 0A 03 00 01 0A 02 01 CE"
    f"SMCIPMITool.exe 1.2.3.4 ADMIN ADMIN ipmi raw 30 68 0A 01 00 01 0A 02 01 CD"

    #Set DNS mode
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 11 00" #DNSv6 Auto
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 11 01" #DNSv6 Manual
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 21 00" #DNSv4 Auto
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 21 01" #DNSv4 Manual
    pass


def test_smcipmitool_30_68_0a_get():
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 10" #AUTO
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 20" #MANUAL
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 00 00"
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 02 00"
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 00 01"
    f"SMCIPMITool.exe 172.31.40.95 ADMIN ADMIN ipmi raw 30 68 0A 02 01"

    dns_ipv4_1 = '' #用api抓ip str
    dns_ipv4_2 = ''
    dns_ipv6_1 = ''
    dns_ipv6_2 = ''

def raw_byte_array():
    value = input('Input 30 68 0A return code: ')
    excepted = input('Input IP address: ')
    value = value.strip()
    Value_NoSpace = ''.join(value.split())
    Transfer_value = bytearray.fromhex(Value_NoSpace).decode()
    if Transfer_value == excepted:
        print(f"Both values match")
    else:
        print(f"{Transfer_value} != {excepted}")

