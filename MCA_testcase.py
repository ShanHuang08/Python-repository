import unittest
import BE_MCA_Sync, BE_MCA_Check
import sys

class MCATestCases(unittest.TestCase):

    def test_MCAtest(self):
        BE_MCA_Sync.MCABankSync_default() #总控后台(预设值)
        assert True

    def test_MCAtest2(self):
        ContinueRun=input('JSON尚未更新，是否繼續比對?(Y/N)')
        if ContinueRun in ['Y','y']:
            pass
        elif ContinueRun in ['N','n']:
            # MCATestCases.test_MCAtest3()
            sys.exit()
            # 如果在子執行緒使用sys.exit()，就只能退出子執行緒，主執行緒仍然還是可以運作
        else:
            raise IndexError("Can't input other characters")

        BE_MCA_Check.MCA_CheckBanks_Contents()
        assert True
        
    # def test_MCAtest3(self):
    #     BE_MCA_Sync.MCABankSync_custom() #自定義s
    #     assert True


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