from robot_run import run
from SeleniumLibrary import SeleniumLibrary
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

# BuiltIn().set_library_search_order(SeleniumLibrary)

def Testlog():
    BuiltIn().run_keyword('Log', 'run_keyword() Hello, World!')
    run('Log', 'run() Hello, World!')

@keyword('This is a new keyword')
def testlog2():
    run('Log', 'run() Hello, World!')
