from pysnmp.proto import rfc1902

Path = {
    'Privacy' : {
        'Advance' : 'details-button',
        'Go ahead' : 'proceed-link'
    },
    'Login' : {
        'username' : 'usrName',
        'password' : 'pwd',
        'Button' : 'login_word'
    },
    'Account Services' : {
        'Users' : {},
        'Directory Services' : {
            'Tab' : 'directoryTab',
            'LDAP' : {
                'Bind DN' : 'ldapDN',
                'Bind Password' : 'pwdLDAP',
                'Username Attribute' : 'usernameattr',
                'Server Add' : 'btnAddrLDAP',
                'Ip add' : 'ip',
                'Server Save' : 'saveBtn', #要用xpath
                'Search Base Add' :'btnBaseLDAP',
                'Base add' : 'base',
                'Save2' : 'xpath',
                'Rules Add' : 'btnRuleLDAP',
                'Admin' : 'role1',
                'Operator' : 'role2',
                'User' : 'role3',
                'Remote User' : 'user',
                'Remote Group' : 'group',
                'Submit' : '//*[@id="btnSubmitLDAP"]'
            },
            'AD' : {},
            'RADIUS' : {}
        }
    }
}


goPage = {
    'Dashboard' : 'goPage("dashboard")',
    'Component info' : 'goPage("sys_cmpn_overview")',
    'Account Services' : 'goPage("config_account_overview")',
    'Remote Control' : 'goPage("remote")',
    'Storage' : 'goPage("sys_storage")'
}


redfish = {
    "Accounts" : "/redfish/v1/AccountService/Accounts/",
    "Systems" : "/redfish/v1/Systems/1/",
    "MD5_DES" : {"UserName" : "SnmpUser", 
                 "Password" : "Suser123", 
                 "RoleId" : "Administrator", 
                 "Enabled" : True, 
                 "AccountTypes" : ["SNMP"], 
                 "SNMP" : {"AuthenticationKey": "Aa123456", "EncryptionKey": "Aa123456", "AuthenticationProtocol": "HMAC_MD5", "EncryptionProtocol": "CBC_DES"}
                 },
    "SNMP" : "/redfish/v1/Managers/1/NetworkProtocol",
    "Enable SNMP" : {"SNMP" : {"ProtocolEnabled": True}},
    "Add SNMPv2 Community" : {"SNMP" : {
                        "EnableSNMPv2c" : True,
                        "CommunityStrings" : [
                            {
                                "AccessMode": "Full",
                                "CommunityString": "Public",
                                "Name": "V2Test"
                            }
                        ]
                    }
    },
    "Enable SNMPv3" : {
        "SNMP" : {
            "EnableSNMPv3": True,
            "AuthenticationProtocol": "HMAC_MD5",
            "EncryptionProtocol": "CBC_DES"
        }
    },
    "Disable SNMP" :{
        "SNMP" :{
            "EnableSNMPv3": False,
            "CommunityStrings": [],
            "EnableSNMPv2c" : False,
            "ProtocolEnabled": False
        }
    },
    "LDAP Setup" : {
    "LDAP": {
        "ServiceEnabled": True,
        "ServiceAddresses": [
            "ldap://10.140.168.235:389"
        ],
        "Authentication": {
            "Username": "cn=Manager,dc=ipmi,dc=com",
            "Password": "secret"
        },
        "RemoteRoleMapping": [
            {
                "RemoteUser": "Admin",
                "LocalRole": "Administrator"
            },
            {
                "RemoteUser": "Operator",
                "LocalRole": "Operator"
            },
            {
                "RemoteUser": "User",
                "LocalRole": "ReadOnly"
            }
        ],
        "LDAPService": {
            "SearchSettings": {
                "BaseDistinguishedNames": [
                    "dc=ipmi,dc=com"
                ],
                "UsernameAttribute": "cn"
            }
        }
    }
    },
    "LDAP clear" : {
    "LDAP": {
        "ServiceEnabled": False,
        "ServiceAddresses": [],
        "Authentication": {
            "Username": "",
            "Password": ""
        },
        "RemoteRoleMapping": [],
        "LDAPService": {
            "SearchSettings": {
                "BaseDistinguishedNames": [],
                "UsernameAttribute": ""
            }
        }
    }
    }


}

OID = {
    "uid on" : rfc1902.Unsigned32(1),
    "uid off" :  rfc1902.Unsigned32(0)
}


SUT = {
    "X12SPW-F" : {
        "BMC" : "10.184.15.152",
        "OS" : "10.184.26.174"
    },
    "X12STE-F" : {
        "BMC" : "10.184.30.82",
        "OS" : "10.184.27.100"
    },
    "X12STE-F Sys" :{
        "BMC" : "10.184.13.92",
        "OS" : "10.184.12.161"
    },
    "X13SET-G" : {
        "BMC" : "10.184.27.76",
        "OS" : "10.184.28.81"
    },
    "X12SPO-NTF" : {
        "BMC" : "10.184.16.44",
        "OS" : "10.184.24.227"
    },
    "X12SPG-NF" : {
        "BMC" : "10.184.21.109",
        "OS" : "10.184.18.96"
    },
    "X13SCL-IF" : {
        "BMC" : "10.184.19.24",
        "OS" : "10.184.20.92"
    },
    "H13SSH" : {
        "BMC" : "172.31.37.193",
        "OS" : "172.31.49.17"
    },
    "H12DGO-6" : {
        "BMC" : "172.31.53.18",
        "OS" : "172.31.41.47"
    }
}


'''
Server Address
//*[@id="formAddr"]/div[4]
//*[@id="saveBtn"]

Search Base
//*[@id="formBase"]/div[2]
//*[@id="saveBtn"]

Rules
//*[@id="formRule"]/div[4]

Submit
//*[@id="btnSubmitLDAP"]
'''