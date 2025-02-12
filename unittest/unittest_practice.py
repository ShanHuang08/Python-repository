import unittest
from selenium import webdriver
def test_aaa(a):
    print('Test1')

def test_bbb():
    print('Test2')

class PythonMainPage(unittest.TestCase):
    def setUp(self) -> None:
        pass
          
    def test1(self):
        test_aaa()
        test_bbb()
        assert True

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
    
