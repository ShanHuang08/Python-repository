from Library.dictionary import RawCommands
from Library.Strings import Check_PWD

server_ip = input('Input SUT ip: ')



def ShowRawCommands():
    # auth = Check_PWD(server_ip)
    auth = ('ADMIN', 'ADMIN')
    print(RawCommands["0A"] + ' Get:')
    for cmd in RawCommands['DNS Mode']:    
        if cmd != '20':
            print(f'SMCIPMITool.exe {server_ip} ADMIN {auth[1]} {RawCommands["0A"]} {cmd}')  
            
    print(RawCommands["0A"] + ' Set:')
    for name, num in RawCommands['DNS']:
        if num == '01':
            print(name)
        else:
            print(name)             
        for ip in RawCommands['ipv4']:
            print(f'SMCIPMITool.exe {server_ip} ADMIN {auth[1]} {RawCommands["0A"]} {num} 00 00 {ip}')
        for ip in RawCommands['ipv6']:
            print(f'SMCIPMITool.exe {server_ip} ADMIN {auth[1]} {RawCommands["0A"]} {num} 01 00 {ip}')
    
    for name, cmd in RawCommands['09 Get Set']:
        if name in ['Add IPv6', 'Delete IPv6']:
            if name == 'Add IPv6':
                print(RawCommands["09"] + ' Set:')
            print(f'{name}\nSMCIPMITool.exe {server_ip} ADMIN {auth[1]} {RawCommands["09"]} {cmd} {RawCommands["ipv6"][0]} {hex(64)[2:]}')
        elif 'Set Gateway' in name:
            print(f'{name}\nSMCIPMITool.exe {server_ip} ADMIN {auth[1]} {RawCommands["09"]} {cmd} {RawCommands["ipv6"][3]}')
        else:
            if cmd == '00 00':
                print(RawCommands["09"] + ' Get:')
            print(f'{name}\nSMCIPMITool.exe {server_ip} ADMIN {auth[1]} {RawCommands["09"]} {cmd}')   

ShowRawCommands()

def set_ipv6_data(dhcp_mode:str, auto_config:str, ipv6_opation:str, address:str, prefix:str):
    print((f'30 68 09 01 {dhcp_mode} {auto_config} {ipv6_opation} {address} {prefix}'))

def set_ipv6_gateway(gateway:str):
    print(f'30 68 09 02 {gateway}')

def get_ipv6_data(data:str):
    print(f'30 68 09 00 {data}')
    pass

def prefix(num):
    return hex(num)[2:]

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



