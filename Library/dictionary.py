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
    'Storage Monitoring' : 'goPage("sys_storage")',
    'Multi Node' : 'goPage("sys_multinode")'
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
    },
    "Alert SNMPv1" : {
        "Destination" : "10.184.11.130",
        "Protocol": "SNMPv1",
        "EventTypes": [
            "Alert"
        ],
        "SNMP": {
            "TrapCommunity": "test"
        },
        "Oem": {
            "Supermicro": {
                "Severity": "Information",
                "EnableSubscription": True
            }
        }
    },
    "Create user01" : {"UserName": "user01", "Password": "Suser123", "RoleId": "Operator", "Enabled": True, "AccountTypes": ["Redfish"]},
    "Create user02" : {"UserName": "user02", "Password": "Suser123", "RoleId": "ReadOnly", "Enabled": True, "AccountTypes": ["Redfish"]},
    "CertificateString" : [
        "-----BEGIN CERTIFICATE-----\nMIIFuTCCA6GgAwIBAgIUGRevjh+gqtXiy4MWqjlVpItH8EEwDQYJKoZIhvcNAQEL\nBQAwazELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExETAPBgNVBAcM\nCFNhbiBKb3NlMQ0wCwYDVQQKDARTTUNJMQ0wCwYDVQQLDARTV1FBMRYwFAYDVQQD\nDA1IVFRQU0JPT1RURVNUMCAXDTI0MDYxNzIyMTQzN1oYDzIxMjQwNTI0MjIxNDM3\nWjBrMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTERMA8GA1UEBwwI\nU2FuIEpvc2UxDTALBgNVBAoMBFNNQ0kxDTALBgNVBAsMBFNXUUExFjAUBgNVBAMM\nDUhUVFBTQk9PVFRFU1QwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDD\nZqLNGB3/a+zOmKQDW/F4qxy1QCh+3iyX+E/aTNA3b+jZ8+qj/4PmUfDSGq564G4U\n1C8vD3aREL9JgyqOgvHZHo7jojwvr+SJIc/O5On7Qcwf37CwbdPqTv1aJAInNUN7\nP2DRzG2SmQRBMs8JmC0Vs9iOca4gCMsB3+dGIvwTRXnoCcNRjO0IAsbyPXiyTB1k\nDiqv95M9W3mlzggbNAtFz2EibYwCj5+W5GAYvMXQc6EXsiDPY3mq7WeqofbyKqta\nRE+Dw544qTae7E7zmBgyl67+J1WNJYa9urwbEsZEbXy7bMo38TLP+YJYsfvfcJxT\n4vmZi7eP/y6fn6mmgBERt9RPlFS12URRelkvKiwLsreAxfu1SSHF36WNOFKCu28W\n8hM3h/DCRr53z+mlC6xF5HnMvT2qHCoHDyRwSvDiuHqKNQ7L9a425N1s5aLmx8Gr\nRaylgYnl7aQnrhWNQk2RbjnToqw3v2wHBGuaoscCbKTmC387UqN3TsvdE3HLyc6Y\nKwP3aIb6NWah3X1kITJzp7OcE9t96s/fYt2i89V4KJm+9Xw6z2QgQQJcshxndlmF\nQyWx84ELde/6c+hDilDtaCC+gb0jS45qKsx2rz30I4IqMpXWjuOpoAzeqq6vB+fK\nV21LekLdlwBBBKHtS/tyV/zcko+YUvB+aLGgkO9FbwIDAQABo1MwUTAdBgNVHQ4E\nFgQUTkws0fLS56AJ9XnAdzQcuBpiw78wHwYDVR0jBBgwFoAUTkws0fLS56AJ9XnA\ndzQcuBpiw78wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAgEAub7P\nxkYKz+hiE/s0MGtK9kCcr/2zmeZJS4zst+GzyjA6cfW5ISH39tm3PlvkPxIuHhKr\nRoQM2zEzP8iw8V+hieyyMIYCEDuHLqfaPCIoJUD/Y3G3xzvwwIeWOA+KqblvsDz5\naPY4RjK1lYJH4TAS/SbQwHVCEx0D5DiusKzrvE8wrzpelZFJJ9i3Hh4sIy+IibwM\n7yegL6d9r3b3M1TqdddeuLfxeoOTp5SW0ePeHNml1kiv5MfUCsYsXHWnwGOoOyHr\nEntjH3QJ6a6/AjapomRs/h0luwWEpx5zhA0R44fiuT/Wu8xmh0Qaln3JMhUkVDBA\nc2OBnw75B2OfQ5A6DEdmYpfbWPGTHNtt+aPhLLhiJeUgXSxDxyrk9Dg8DWOQwyRQ\n+24leFVL2Q3MUV+aEEUeG393RqlFqp6Fof4kfQ+ba4pkcWx8MdPvp9drlR5blvf1\nP6JPY+iJxYEWw3RJtOzCcTSt9fL+uxQh7J7s8lK1OR8J+wtWsnBpwysguhcfNei1\n62E++V88Z+4Mx4Vpk9V2cOJDnW8oDhOc2gscfphyy4Vj8Cta6SfsqITc+gI9BzO1\nU4hUzxlETWFGFsEqeb71Jbx5Fi9Z4gM058nHNfMb3LexUlxM0o98xKUPcQ4WD4pm\n9UkkZ+BhNQcKxyEHiovfueeMqxxYaRpWlXSrBP0=\n-----END CERTIFICATE-----",
        "-----BEGIN CERTIFICATE-----\nMIIDvzCCAqegAwIBAgIUbfU5fCSjALNseAKfjyFLNq3TWRswDQYJKoZIhvcNAQELBQAwbjELMAkGA1UEBhMCVFcxCzAJBgNVBAgMAlRXMQwwCgYDVQQHDANUUEUxDTALBgNVBAoMBFNNQ0kxCjAIBgNVBAsMAUExEzARBgNVBAMMClN1cGVybWljcm8xFDASBgkqhkiG9w0BCQEWBWFAYi5jMCAXDTIzMDEzMDA5MzUyMVoYDzMwMjIwNjAyMDkzNTIxWjBuMQswCQYDVQQGEwJUVzELMAkGA1UECAwCVFcxDDAKBgNVBAcMA1RQRTENMAsGA1UECgwEU01DSTEKMAgGA1UECwwBQTETMBEGA1UEAwwKU3VwZXJtaWNybzEUMBIGCSqGSIb3DQEJARYFYUBiLmMwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDikgPyeJw9aNLWug0RLp6FZhkX+W2iesg6iuiOgZw1byI6HTxsm2ANjFpBfIhauIqSCnYSuc+KaNdQhyn3NlpiT9uQikMCv/pYuSAwcBsjVOeLPS4BcMCUXNZqT20HMHgf1JIHY/SMknqst2sLp/fa643SKO9V2YsgHVm0oqyAnSlHO4QyuRd4SE4dj/Yi2E5fZJwSHs4RO9Xn6oUCSHDnB9wFn6grRsABEO/y1f+p92Fn7Q7Il2p0EbXiMEW3SBVohJMssTkaMRvzMXT2cSrG6l9r9TaUi7NuM6YnA91EJQ8gtKTjFQCCYkS7fEPchcM/slHVKNFCw6CtHfu7hlglAgMBAAGjUzBRMB0GA1UdDgQWBBTOK8iiTOmyKJnmzQtEgvWSKdMQ5jAfBgNVHSMEGDAWgBTOK8iiTOmyKJnmzQtEgvWSKdMQ5jAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQB4bq5Wgqu9rt+GoAwVbem8drF34nG0SFofiHHB4u9sgqThr3XtBimmB7CgOKApYDXHdHzy/LNQBxr8WnsYSr8NAswT9cd+ZMZl9s091wVRmANIQz8Yi/ySooII9k1QmzMYyslgCTGhkk7OP0bWGggZVA/8eQXHKfluhT0WS0wGSchqpXZwLOcWsTn87iePaeWWWaCqDGJSOLNTlC7teWQNMnnC0N98XcMVgP0bGdyoPZaiujpVG9pYdug3FUhS+PBZ72ArCHzTMD2/WVK/JXntVd/H9jZSgk0S2ZmnB42TYMHZUV6Y982DorKa5WZZSJvVMXGSiCuuIfkfSO65Kl6f\n-----END CERTIFICATE-----"
    ]


}

OID = {
    "uid on" : rfc1902.Unsigned32(1),
    "uid off" :  rfc1902.Unsigned32(0)
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

text = 'qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwer@qwert.qqq'
# text = 'qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwer@abc.com'
# text = 'qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwer@qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwe.qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwe.qwert1'
# text = 'qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwer@qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwe.qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwe.qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qw'
# text = 'hi-there-yes-you-information-abcdefghijklmnopqrstuvwxyz@please-try-to.send-me-an-email-if-you-can-possibly-begin-to-remember-this-coz.this-is-the-longest-email-address-known-to-man-but-to-be-honest.this-is-such-a-stupidly-long-sub-domain-forever.parco.com'