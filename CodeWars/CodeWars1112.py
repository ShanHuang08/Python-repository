import unittest
from random import randint
def question1(operator, value1, value2):
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

# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).
# ex:None=>0, []=>0, [3]=>0 [-3]=>0, [ 3, 5]=>0, [6, 2, 1, 8, 10]=>16
def question2(arr):
    #your code here
    if arr != None:
        if arr != []:
            Sum=0
            for i in range(len(arr)):
                Sum+=arr[i]
            Sum = Sum-max(arr)
            if Sum != 0:
                Sum = Sum-min(arr)
            return Sum
        else:
            return 0
    else:
        return 0

def sum_array2(arr):
    #your code here
    if arr == None or len(arr) == 0:
        return 0
    else:
        Sum=0
        for i in range(len(arr)):
            Sum+=arr[i]
            if arr[0] > arr[i] and arr[0] != arr[i]:
                MaxNum=arr[0]
            else:
                MaxNum=arr[i]
            if arr[0] < arr[i] and arr[0] != arr[i]:
                MinNum=arr[0]
            else:
                MinNum=arr[i]
        Sum = Sum-MaxNum
        if Sum != 0:
            Sum = Sum-MinNum
        return Sum

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

def sum_array3(arr):
    if len(arr or []) <= 2:
        return 0

    odd = len(arr) % 2

    if odd:
        total = lowest = highest = arr[0]
    else:
        total, lowest, highest = 0, float('inf'), -float('inf')

    for a, b in zip(arr[odd::2], arr[1 + odd::2]):
        total += a + b
        if a > b:
            lowest = min(b, lowest)
            highest = max(a, highest)
        else:
            lowest = min(a, lowest)
            highest = max(b, highest)

    return total - lowest - highest

def ftMax(a, b):
    if a > b:
        return a
    return b

def ftMin(a, b):
    if a < b:
        return a
    return b

def ftMaxArr(arr):
    maxNumber = arr[0]
    for elem in arr:
        maxNumber = ftMax(maxNumber, elem)
    return maxNumber

def ftMinArr(arr):
    minNumber = arr[0]
    for elem in arr:
        minNumber = ftMin(minNumber, elem)
    return minNumber

def sum_array4(arr):
    if not arr or len(arr) == 1:
        return 0
    maxResult = ftMaxArr(arr)
    minResult = ftMinArr(arr)
    number = 0
    trigerMax = True
    trigerMin = True
    for elem in arr:
        if elem == maxResult and trigerMax:
            trigerMax = False
            continue
        if elem == minResult and trigerMin:
            trigerMin = False
            continue
        number += elem
    return number

# [1,2,3,4]=>1*2*3*4=24
def grow(arr):
    while len(arr) > 1:
        arr[1] = arr[0] * arr[1]
        arr = arr[1:]
        print(arr)
    return arr[0]

def grow2(arr):   
    flag = arr[0]
    for i in arr[1:]:
        flag *= i
      
    return flag 

class testcases(unittest.TestCase):
    def test_Basic_Test(self):
        self.assertEqual(question1('+',2,3), 5)
        self.assertEqual(basic_op('-',2,3), -1)
        self.assertEqual(basic_op2('+',2,3), 5)
        self.assertEqual(question1('*',2,3), basic_op('*',2,3))

    def test_Random_test_for_op(self):
        operators='+-*/'
        sol=lambda op, v1, v2: eval("".join([str(v1),op,str(v2)])) #公式
        sol2=lambda op, v1,v2: eval("{}{}{}".format(v1, op, v2)) #公式2
        sol3=lambda op, v1,v2: question1(op,v1,v2) #呼叫公式
        for i in range(20):
            op,v1,v2=operators[randint(0,3)],randint(1,10**randint(1,5)),randint(1,10**randint(1,5))
            self.assertEqual(question1(op,v1,v2), sol(op,v1,v2))
            self.assertEqual(basic_op(op,v1,v2), sol(op,v1,v2))

            self.assertEqual(question1(op,v1,v2), sol2(op,v1,v2))
            self.assertEqual(basic_op(op,v1,v2), sol2(op,v1,v2))

            self.assertEqual(question1(op,v1,v2), sol3(op,v1,v2))
            self.assertEqual(basic_op(op,v1,v2), question1(op,v1,v2))

    def test_um_array_basic(self):
        self.assertEqual(sum_array3(None), 0)
        self.assertEqual(sum_array3([]), 0)
        
        self.assertEqual(sum_array4(None), 0)
        self.assertEqual(sum_array4([]), 0)

    def test_um_array_random(self):
        RandomList=[]
        for i in range(40):
            for j in range(randint(0, 10)):
                RandomList.append(randint(-10**2, 10**2))
            
            self.assertEqual(sum_array3(RandomList), sum_array(RandomList))
            self.assertEqual(sum_array4(RandomList), sum_array(RandomList))

if __name__=='__main__':
    unittest.main()


# random sample
# testdigit=random.sample(range(1,50), random.randint(1,5))
# print(testdigit)

# List=[]
# for i in range(random.randint(1,5)):
#     List.append(random.randint(1,50))
# print(List)