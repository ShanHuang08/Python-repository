from robot.libraries.BuiltIn import BuiltIn
from robot_run import run
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from time import sleep
import sys
sys.path.append('C:\\Users\\Shan\\Workspace2\\Python-repository')
from test0630 import MyLibrary
# print(sys.path)

BuiltIn().set_library_search_order(SeleniumLibrary, MyLibrary)
# BuiltIn().set_library_search_order(SeleniumLibrary)

@keyword('Sleep time')
def my_sleep(secs):
    sleep(secs)


def Testlog():
    BuiltIn().run_keyword('Log', 'run_keyword() Hello, World!')
    run('Log', 'run() Hello, World!')

@keyword('This is a new keyword')
def testlog2():
    run('Log', 'run() Hello, World!')
    run('Open Browser', 'https://www.google.com', 'chrome')
    run('Sleep time', 3)
    run('Close Browser')

def MyLibrary0630(self):
    MyLibrary.MySolution(self)
    MyLibrary.ChatGPT(self)


