from robot.libraries.BuiltIn import BuiltIn

def run(name, *args):
    return BuiltIn().run_keyword(name, *args)

def var(var_name, default=None):
    return BuiltIn().get_variable_value(var_name, default=default)




# run('SUT Type')


# 在 Python 中，print() 函式用於將文字輸出到終端或標準輸出流。它將輸出的結果打印到終端，並通常不返回任何值。

# 另一方面，return 關鍵字用於在函式中返回值。當函式達到 return 陳述時，它將結束函式的執行並返回指定的值。

# 在你提到的情況下，使用 print() 並不能將結果返回給調用函式的地方。如果你只是使用 print(f'')，它只會在終端上打印結果，而不會返回給外部程式碼。

# 相反，使用 f'' 語法，可以將結果作為字串返回給調用方。這樣外部程式碼就可以接收到該值並進行後續處理。

# 簡而言之，print() 是用於打印到終端的函式，而 return 是用於從函式中返回值的關鍵字。在你的程式中，你希望將結果返回給外部程式碼，因此應使用 return 陳述並將結果包含在 f'' 中以返回字串值。

# raceback (most recent call last):
#   File "c:\Users\Stephenhuang\Python\Robot\test.py", line 25, in <module>
#     run('SUT_Type', SUT)
#   File "c:\Users\Stephenhuang\Python\Robot\test.py", line 9, in run
#     return BuiltIn().run_keyword(name, *args)
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\robot\libraries\BuiltIn.py", line 1847, in run_keyword
#     and not self._context.dry_run
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\robot\libraries\BuiltIn.py", line 59, in _context
#     return self._get_context()
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\robot\libraries\BuiltIn.py", line 64, in _get_context
#     raise RobotNotRunningError('Cannot access execution context')
#   File "c:\Users\Stephenhuang\Python\Robot\test.py", line 25, in <module>
#     run('test_keyword')
#   File "c:\Users\Stephenhuang\Python\Robot\test.py", line 9, in run
#     return BuiltIn().run_keyword(name, *args)
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\robot\libraries\BuiltIn.py", line 1847, in run_keyword
#     and not self._context.dry_run
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\robot\libraries\BuiltIn.py", line 59, in _context
#     return self._get_context()
#   File "C:\Users\Stephenhuang\AppData\Local\Programs\Python\Python310\lib\site-packages\robot\libraries\BuiltIn.py", line 64, in _get_context
#     raise RobotNotRunningError('Cannot access execution context')
# robot.libraries.BuiltIn.RobotNotRunningError: Cannot access execution contex
