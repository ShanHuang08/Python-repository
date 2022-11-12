import unittest
from random import randint
def main(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

def basic_op2(operator, value1, value2):
    return eval("".join([str(value1),operator,str(value2)]))


class testcases(unittest.TestCase):
    def test_Basic_Test(self):
        self.assertEqual(main('+',2,3), 5)
        self.assertEqual(basic_op('-',2,3), -1)
        self.assertEqual(basic_op2('+',2,3), 5)
        self.assertEqual(main('*',2,3), basic_op('*',2,3))

    def test_Random_test(self):
        operators='+-*/'
        sol=lambda op, v1, v2: eval("".join([str(v1),op,str(v2)])) #公式
        sol2=lambda op, v1,v2: eval("{}{}{}".format(v1, op, v2)) #公式2
        sol3=lambda op, v1,v2: main(op,v1,v2) #呼叫公式
        for i in range(20):
            op,v1,v2=operators[randint(0,3)],randint(1,10**randint(1,5)),randint(1,10**randint(1,5))
            self.assertEqual(main(op,v1,v2), sol(op,v1,v2))
            self.assertEqual(basic_op(op,v1,v2), sol(op,v1,v2))

            self.assertEqual(main(op,v1,v2), sol2(op,v1,v2))
            self.assertEqual(basic_op(op,v1,v2), sol2(op,v1,v2))

            self.assertEqual(main(op,v1,v2), sol3(op,v1,v2))
            self.assertEqual(basic_op(op,v1,v2), main(op,v1,v2))

if __name__=='__main__':
    unittest.main()