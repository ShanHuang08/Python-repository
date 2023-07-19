from robot_run import run
from SeleniumLibrary import SeleniumLibrary
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
# from test0630 import MyLibrary


BuiltIn().set_library_search_order(SeleniumLibrary)
# BuiltIn().set_library_search_order(SeleniumLibrary(), MyLibrary())

def Testlog():
    BuiltIn().run_keyword('Log', 'run_keyword() Hello, World!')
    run('Log', 'run() Hello, World!')

@keyword('This is a new keyword')
def testlog2():
    run('Log', 'run() Hello, World!')
