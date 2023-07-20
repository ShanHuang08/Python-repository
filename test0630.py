from Method.test_method import *
from Robot.robot_run import run
from robot.api.deco import keyword

A = 'Type1'
B = 'Type2'
C = '123'
SUT = A

class MyLibrary():
    def __init__(self) -> None:
        pass

    def MySolution(self):
        message = 'hello,world'
        List = message.split(',')
        message_1 = List[0].replace(List[0], List[1])
        message_2 = List[1].replace(List[1], List[0])

        new_message = message_1 + ',' + message_2
        print(new_message)


    def ChatGPT(self):
        message = 'hello,world'
        index = message.index(',')  # 找到逗號的索引位置
        print(index)
        new_message = message[index + 1:] + ',' + message[:index]

        print(new_message)


    def FailedCase(self):
        message = 'hello,world'
        index = message.index(',')  # 找到逗號的索引位置
        print(index)
        new_message = message[index + 1:] + ',' + message[:index]

        print(new_message)



    @keyword('Test SUT Type')
    def SUT_Type(self):
        if SUT not in A or B:
            return f'{SUT} != {A} and {B}'
        else:
            return f'{SUT}'

    @keyword('Test Keyword')
    def test_keyword(self):
        run('Log', 'Hello, World!')
        run('Sleep', 1)

if __name__=='__main__':
    # MySolution()
    # ChatGPT()
    # Add(4,5)
    pass

