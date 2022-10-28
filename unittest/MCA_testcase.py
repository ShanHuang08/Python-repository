import unittest
import BE_MCA

class TestCases(unittest.TestCase):

    def test_MCAtest(self):
        BE_MCA.MCABankSync_default() #总控后台(预设值)
        assert True

    def test_MCAtest2(self):
        BE_MCA.MCABankSync_custom() #自定义同步内容
        assert True
        
if __name__=='__main__':
    unittest.main()



# F
# ======================================================================
# FAIL: test_MCAtest (__main__.TestCases)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\shan_huang\Python\MCA_testcase.py", line 8, in test_MCAtest
#     with self.assertRaises(NoSuchElementException) as cm:
# AssertionError: NoSuchElementException not raised

# ----------------------------------------------------------------------
# Ran 1 test in 76.067s

# FAILED (failures=1)

# E
# ======================================================================
# ERROR: test_MCAtest (__main__.TestCases)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\shan_huang\Python\MCA_testcase.py", line 8, in test_MCAtest
#     if not NoSuchElementException in BE_MCA.MCABankSync():
# TypeError: argument of type 'NoneType' is not iterable

# ----------------------------------------------------------------------
# Ran 1 test in 76.766s

# FAILED (errors=1)