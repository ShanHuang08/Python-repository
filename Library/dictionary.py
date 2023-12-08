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
    },
    "X12SPA-TF Win10" : {
        "BMC" : "10.184.14.49",
        "OS" : "10.184.11.130"
    },
    "A2SDi-H-TF Centos" : {
        "BMC" : "10.184.19.52",
        "OS" : "10.184.24.65"
    },
    "X13DSF-A sys" : {"BMC" : "172.31.42.242", "OS" : "172.31.52.73"},
    "X13SEDW-F sys" : {"BMC" : "172.31.40.95", "OS" : "172.31.50.14"},
    'H13SSW-P': {'BMC': '10.184.28.110', 'OS': '10.184.28.34'},
    'X13SEDW-F': {'BMC': '10.140.172.172', 'OS': '10.140.168.150'},
    'X13SWA-TF sys': {'BMC': '172.31.33.188', 'OS': '172.31.32.233'},
    'X13SWA-TF': {'BMC': '10.184.26.167', 'OS': '10.184.14.198'},
    'X12SCA-5F': {'BMC': '10.184.29.149', 'OS': '10.184.14.244'},
    'H12DSG-O-CPU': {'BMC': '172.31.35.46', 'OS': '172.31.35.181'},
    'X13DET-B': {'BMC': '10.184.16.55', 'OS': '10.184.21.44'},
    'X13SCH-SYS sys': {'BMC': '10.184.20.214', 'OS': '10.184.26.232'},
    'H13SSL-N': {'BMC': '10.184.29.232', 'OS': '10.184.28.188'},
    'X12DPL-i6': {'BMC': '10.184.29.186', 'OS': '10.184.21.203'},
    'H13SST-G sys': {'BMC': '172.31.35.83', 'OS': '172.31.32.61'},
    'X12STD-F': {'BMC': '10.184.26.116', 'OS': '10.184.13.142'},
    'X12SPi-TF': {'BMC': '10.184.12.155', 'OS': '10.184.27.208'}
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

RawCommands = {
    '30 68 0A' : {
        'Get' : {
            'DNS Mode' : ['10', '20', '00 00', '02 00', '00 01', '02 01']
        },
        'Set' : {
            'DNS1' : '01', 
            'DNS2' : '03',
            'Add DNSv4' : '00 00', 
            'Del DNSv4' : '00 01',
            'Add DNSv6' : '01 00',
            'Del DNSv6' : '01 01',
            'IPv4' : ['00 00 00 00', 'FF FF FF FF', '0A 02 01 CE'],
            'IPv6' : ['20 11 00 00 00 00 00 00 00 00 00 00 00 00 11 11',
                    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02',
                    'FE FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF',
                    '20 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01',
                    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00',
                    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01',
                    'FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00',
                    'FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF',
                    'FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01'],
        }
    },

    '30 68 09' : {
        'Get' : {
            'DHCP Mode' : '00 00',
            'Auto Config' : '00 01',
            'Address list' : '00 02',
            'Duid' : '00 03',
            'Gateway' : '00 04'
        },
        'Set' : {
            'Add' : '01 02 00 00',
            'Delete' : '01 02 00 01',
            'Gateway' : '02',
            'IPv6' : ['20 11 00 00 00 00 00 00 00 00 00 00 00 00 11 11',
                      '20 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01'],
            'Prefix' : '40'
        }
    },
}

timezones = {
    "-12:00": ["(UTC-12:00) International Date Line West"],
    "-11:00": ["(UTC-11:00) Coordinated Universal Time-11"],
    "-10:00": ["(UTC-10:00) Aleutian Islands", "(UTC-10:00) Hawaii"],
    "-09:30": ["(UTC-09:30) Marquesas Islands"],
    "-09:00": ["(UTC-09:00) Alaska", "(UTC-09:00) Coordinated Universal Time-09"],
    "-08:00": [
        "(UTC-08:00) Baja California",
        "(UTC-08:00) Coordinated Universal Time-08",
        "(UTC-08:00) Pacific Time (US & Canada)"],
    "-07:00": [
        "(UTC-07:00) Arizona",
        "(UTC-07:00) Chihuahua, La Paz, Mazatlan",
        "(UTC-07:00) Mountain Time (US & Canada)",
        "(UTC-07:00) Yukon"],
    "-06:00": [
        "(UTC-06:00) Central America",
        "(UTC-06:00) Central Time (US & Canada)",
        "(UTC-06:00) Easter Island",
        "(UTC-06:00) Guadalajara, Mexico City, Monterrey",
        "(UTC-06:00) Saskatchewan"],
    "-05:00": [
        "(UTC-05:00) Bogota, Lima, Quito, Rio Branco",
        "(UTC-05:00) Chetumal",
        "(UTC-05:00) Eastern Time (US & Canada)",
        "(UTC-05:00) Haiti", "(UTC-05:00) Havana",
        "(UTC-05:00) Indiana (East)",
        "(UTC-05:00) Turks and Caicos"],
    "-04:00": [
        "(UTC-04:00) Asuncion",
        "(UTC-04:00) Atlantic Time (Canada)",
        "(UTC-04:00) Caracas",
        "(UTC-04:00) Cuiaba",
        "(UTC-04:00) Georgetown, La Paz, Manaus, San Juan",
        "(UTC-04:00) Santiago"],
    "-03:30": ["(UTC-03:30) Newfoundland"],
    "-03:00": [
        "(UTC-03:00) Araguaina",
        "(UTC-03:00) Brasilia",
        "(UTC-03:00) Cayenne, Fortaleza",
        "(UTC-03:00) City of Buenos Aires",
        "(UTC-03:00) Greenland",
        "(UTC-03:00) Montevideo",
        "(UTC-03:00) Punta Arenas",
        "(UTC-03:00) Saint Pierre and Miquelon",
        "(UTC-03:00) Salvador"],
    "-02:00": ["(UTC-02:00) Coordinated Universal Time-02"],
    "-01:00": ["(UTC-01:00) Azores", "(UTC-01:00) Cabo Verde Is."],
    "+00:00": [
        "(UTC+00:00) Coordinated Universal Time",
        "(UTC+00:00) Dublin, Edinburgh, Lisbon, London",
        "(UTC+00:00) Monrovia, Reykjavik",
        "(UTC+00:00) Sao Tome"],
    "+01:00": [
        "(UTC+01:00) Casablanca",
        "(UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna",
        "(UTC+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague",
        "(UTC+01:00) Brussels, Copenhagen, Madrid, Paris",
        "(UTC+01:00) Sarajevo, Skopje, Warsaw, Zagreb",
        "(UTC+01:00) West Central Africa"],
    "+02:00": [
        "(UTC+02:00) Amman",
        "(UTC+02:00) Athens, Bucharest",
        "(UTC+02:00) Beirut",
        "(UTC+02:00) Cairo",
        "(UTC+02:00) Chisinau",
        "(UTC+02:00) Damascus",
        "(UTC+02:00) Gaza, Hebron",
        "(UTC+02:00) Harare, Pretoria",
        "(UTC+02:00) Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius",
        "(UTC+02:00) Jerusalem",
        "(UTC+02:00) Juba",
        "(UTC+02:00) Kaliningrad",
        "(UTC+02:00) Khartoum",
        "(UTC+02:00) Tripoli",
        "(UTC+02:00) Windhoek"],
    "+03:00": [
        "(UTC+03:00) Baghdad",
        "(UTC+03:00) Istanbul",
        "(UTC+03:00) Kuwait, Riyadh",
        "(UTC+03:00) Minsk",
        "(UTC+03:00) Moscow, St. Petersburg",
        "(UTC+03:00) Nairobi",
        "(UTC+03:00) Volgograd"],
    "+03:30": ["(UTC+03:30) Tehran"],
    "+04:00": [
        "(UTC+04:00) Abu Dhabi, Muscat",
        "(UTC+04:00) Astrakhan, Ulyanovsk",
        "(UTC+04:00) Baku",
        "(UTC+04:00) Izhevsk, Samara",
        "(UTC+04:00) Port Louis",
        "(UTC+04:00) Saratov",
        "(UTC+04:00) Tbilisi",
        "(UTC+04:00) Yerevan"],
    "+04:30": ["(UTC+04:30) Kabul"],
    "+05:00": [
        "(UTC+05:00) Ashgabat, Tashkent",
        "(UTC+05:00) Ekaterinburg",
        "(UTC+05:00) Islamabad, Karachi",
        "(UTC+05:00) Qyzylorda"],
    "+05:30": [
        "(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi",
        "(UTC+05:30) Sri Jayawardenepura"],
    "+05:45": ["(UTC+05:45) Kathmandu"],
    "+06:00": [
        "(UTC+06:00) Astana",
        "(UTC+06:00) Dhaka",
        "(UTC+06:00) Omsk"],
    "+06:30": ["(UTC+06:30) Yangon (Rangoon)"],
    "+07:00": [
        "(UTC+07:00) Bangkok, Hanoi, Jakarta",
        "(UTC+07:00) Barnaul, Gorno-Altaysk",
        "(UTC+07:00) Hovd",
        "(UTC+07:00) Krasnoyarsk",
        "(UTC+07:00) Novosibirsk",
        "(UTC+07:00) Tomsk"],
    "+08:00": [
        "(UTC+08:00) Beijing, Chongqing, Hong Kong, Urumqi",
        "(UTC+08:00) Irkutsk",
        "(UTC+08:00) Kuala Lumpur, Singapore",
        "(UTC+08:00) Perth",
        "(UTC+08:00) Taipei",
        "(UTC+08:00) Ulaanbaatar"],
    "+08:45": ["(UTC+08:45) Eucla"],
    "+09:00": [
        "(UTC+09:00) Chita",
        "(UTC+09:00) Osaka, Sapporo, Tokyo",
        "(UTC+09:00) Pyongyang",
        "(UTC+09:00) Seoul",
        "(UTC+09:00) Yakutsk"],
    "+09:30": ["(UTC+09:30) Adelaide","(UTC+09:30) Darwin"],
    "+10:00": [
        "(UTC+10:00) Brisbane",
        "(UTC+10:00) Canberra, Melbourne, Sydney",
        "(UTC+10:00) Guam, Port Moresby",
        "(UTC+10:00) Hobart",
        "(UTC+10:00) Vladivostok"],
    "+10:30": ["(UTC+10:30) Lord Howe Island"],
    "+11:00": [
        "(UTC+11:00) Bougainville Island",
        "(UTC+11:00) Chokurdakh",
        "(UTC+11:00) Magadan",
        "(UTC+11:00) Norfolk Island",
        "(UTC+11:00) Sakhalin",
        "(UTC+11:00) Solomon Is., New Caledonia"],
    "+12:00": [
        "(UTC+12:00) Anadyr, Petropavlovsk-Kamchatsky",
        "(UTC+12:00) Auckland, Wellington",
        "(UTC+12:00) Coordinated Universal Time+12",
        "(UTC+12:00) Fiji"],
    "+12:45": ["(UTC+12:45) Chatham Islands"],
    "+13:00": [
        "(UTC+13:00) Coordinated Universal Time+13",
        "(UTC+13:00) Nuku'alofa","(UTC+13:00) Samoa"],
    "+14:00": ["(UTC+14:00) Kiritimati Island"]
}
