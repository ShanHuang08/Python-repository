<<<<<<< HEAD
import unittest
from selenium import webdriver

class PythonMainPage(unittest.TestCase):
    def setUp(self) -> None:
        self.browser=webdriver.Chrome('./chromedriver.exe')
        self.browser.get('http://www.python.org')
    
    def test_aaa(self):
        print('Test1')
        assert True
    def test_bbb(self):
        print('Test2')
        assert True

    def tearDown(self) -> None:
        self.browser.close()

if __name__ == '__main__':
    unittest.main()
    
=======
import unittest
from selenium import webdriver

class PythonMainPage(unittest.TestCase):
    def setUp(self) -> None:
        self.browser=webdriver.Chrome('./chromedriver.exe')
        self.browser.get('http://www.python.org')
    
    def test_aaa(self):
        print('Test1')
        assert True
    def test_bbb(self):
        print('Test2')
        assert True

    def tearDown(self) -> None:
        self.browser.close()

if __name__ == '__main__':
    unittest.main()
    
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
