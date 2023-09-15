import re
from datetime import datetime
from lxml import etree
reformat = r"^b'\<([0-9]{1,3})\>([A-Za-z]{3} [0-9 ]{2} \d{2}:\d{2}:\d{2}) ((([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) ([\S\s]+)"

pattern = r'Setting: "<([^>]+)>([^<]+)</\1>"'

path1 = "C:\\Users\\Username\\Documents"  # 一般字串，使用雙反斜線來表示反斜線
path2 = r"C:\Users\Username\Documents"    # 原始字串，反斜線保持原樣
# print("C:\\Users\\Username\\Documents")
# print(r"C:\Users\Username\Documents")

Ori_xml = r'D:\Old\H13SRD-F\01.01.05\bmccfg_0712_1558.xml'

TagName = ['child8', 'child9']
TagValue = ['Newtest', 'test9']

def Get_Extra_Tag():
    # tree = etree.parse(Ori_xml)
    tree = etree.parse('test.xml')
    root = tree.getroot()
    for child in root.iter('User'):
        user_tag  = child.find('Name')
        # user_tag.text = f'<![CDATA[{user_tag.text}]]>'
        user_tag.text = etree.CDATA(user_tag.text)
        # print(user_tag.text)
        TagName.append('Name')
        TagValue.append(user_tag.text)
        pass_tag = child.find('Password')
        if pass_tag.text == '':
            pass_tag.text = etree.CDATA('')
        # print(pass_tag.text)
        TagName.append('Password')
        TagValue.append(pass_tag.text)


def Modify_test():
    parser = etree.XMLParser(strip_cdata=False)
    # tree = etree.parse(Ori_xml)
    tree = etree.parse('test.xml', parser=parser)
    root = tree.getroot()
    for i in range(len(TagName)):
        for child in root.iter(TagName[i]):
            # print(child.tag, child.text)
            child.text = TagValue[i]
    tree.write('bmcccfg.xml', encoding='utf-8', xml_declaration=True, pretty_print=True, method="xml")

# Get_Extra_Tag()
Modify_test()

