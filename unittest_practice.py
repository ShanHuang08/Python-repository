import unittest
from selenium import webdriver

class PythonMainPage(unittest.TestCase):
    def setUp(self) -> None:
        self.browser=webdriver.Chrome('./chromedriver.exe')
        self.browser.get('http://www.python.org')
    
    def test1(self):
        print('Test1')
        assert True
    def test2(self):
        print('Test2')
        assert False
    def test3(self):
        print('Test3')
        assert True

    def tearDown(self) -> None:
        self.browser.close()

if __name__ == '__main__':
    unittest.main()
    
#     http://blog.castman.net/%E6%95%99%E5%AD%B8/2018/01/27/python-name-main.html
