import pyghmi
from pyghmi.ipmi import command

BMC_IP = '10.184.27.76'
rmcp_port = 623
pwd = 'ADMIN'

try:
    SUT_Connect = command.Command(bmc=BMC_IP, userid='ADMIN', password=pwd, port=rmcp_port)
    response = SUT_Connect.get_net_configuration()
    print(f"IPv4:\n{response}")
except pyghmi.exceptions.IpmiException as e:
    print(str(e))

