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
    'Remote Control' : 'goPage("remote")'
}


redfish = {
    "Accounts" : "/redfish/v1/AccountService/Accounts/",
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