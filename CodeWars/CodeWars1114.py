<<<<<<< HEAD
import unittest
from random import randint
def question1(a):
    for i in range(len(a)):
        a[i]= a[i]-(a[i]*2)
    return a

def invert3(lst):
    for i in range(len(lst)):
        lst[i] = -lst[i]
    return lst

def invert(lst):
    return [-x for x in lst]

def invert2(lst):
   return [i*-1 for i in lst]

# def inverttest(lst):
#     return lambda arr:[-x for x in lst]

def question2(List):
    # List=[0,3,4,5]
    Sum=0
    for i in range(len(List)):
        Sum=Sum+(List[i]*List[i])
    return Sum

def square_sum(numbers):
    res = 0
    for num in numbers:
        res = res + num*num
    return res

def square_sum2(numbers):
    return sum(x * x for x in numbers) 

def question3(a,b):
    List=[]
    Sum=a+b
    while Sum > 0: 
        List.append(Sum%2)
        Sum=Sum // 2 
    answer=''
    for i in range(len(List)-1,-1,-1):
        answer=answer+str(List[i])
    return answer

def add_binary(a,b):
    return bin(a+b)[2:]

def add_binary2(a,b):
    return '{0:b}'.format(a + b)

def add_binary3(a, b):
    return format(a + b, 'b')


class testcases(unittest.TestCase):
    def test_question1_Basic(self):
        self.assertEqual(question1([24, 5, 49, 24]), [-24, -5, -49, -24])
        self.assertEqual(invert([24, 5, 49, 24]), [-24, -5, -49, -24])
        # self.assertEqual(inverttest([-1,2,-3]), [1,-2,3]) #AssertionError: <function inverttest.<locals>.<lambda> at 0x000001A09A29B520> != [1, -2, 3]
    def test_question1_Random(self):
        RandomList=[]
        # sol=lambda RandomList:[-x for x in RandomList] lambda後面不要用loop
        for i in range(randint(0,10)):
            RandomList.append(randint(-100,100))

        self.assertEqual(question1(RandomList), invert3(RandomList))
        
        sol2=[-x for x in RandomList]
        self.assertEqual(question1(RandomList), sol2)




if __name__=='__main__':
    unittest.main()
=======
import unittest
from random import randint
def question1(a):
    for i in range(len(a)):
        a[i]= a[i]-(a[i]*2)
    return a

def invert3(lst):
    for i in range(len(lst)):
        lst[i] = -lst[i]
    return lst

def invert(lst):
    return [-x for x in lst]

def invert2(lst):
   return [i*-1 for i in lst]

# def inverttest(lst):
#     return lambda arr:[-x for x in lst]

def question2(List):
    # List=[0,3,4,5]
    Sum=0
    for i in range(len(List)):
        Sum=Sum+(List[i]*List[i])
    return Sum

def square_sum(numbers):
    res = 0
    for num in numbers:
        res = res + num*num
    return res

def square_sum2(numbers):
    return sum(x * x for x in numbers) 

def question3(a,b):
    List=[]
    Sum=a+b
    while Sum > 0: 
        List.append(Sum%2)
        Sum=Sum // 2 
    answer=''
    for i in range(len(List)-1,-1,-1):
        answer=answer+str(List[i])
    return answer

def add_binary(a,b):
    return bin(a+b)[2:]

def add_binary2(a,b):
    return '{0:b}'.format(a + b)

def add_binary3(a, b):
    return format(a + b, 'b')


class testcases(unittest.TestCase):
    def test_question1_Basic(self):
        self.assertEqual(question1([24, 5, 49, 24]), [-24, -5, -49, -24])
        self.assertEqual(invert([24, 5, 49, 24]), [-24, -5, -49, -24])
        # self.assertEqual(inverttest([-1,2,-3]), [1,-2,3]) #AssertionError: <function inverttest.<locals>.<lambda> at 0x000001A09A29B520> != [1, -2, 3]
    def test_question1_Random(self):
        RandomList=[]
        # sol=lambda RandomList:[-x for x in RandomList] lambda後面不要用loop
        for i in range(randint(0,10)):
            RandomList.append(randint(-100,100))

        self.assertEqual(question1(RandomList), invert3(RandomList))
        
        sol2=[-x for x in RandomList]
        self.assertEqual(question1(RandomList), sol2)




if __name__=='__main__':
    unittest.main()
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
