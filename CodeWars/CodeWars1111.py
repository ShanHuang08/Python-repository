# x=1,y=10 => [1,2,3,4,5,6,7,8,9,10] len=10
# x=2,y=5 => [2,4,6,8,10] len=5
import random

def question1(x,n):
    List=[]
    z=x
    for i in range(n):
        List.append(x)
        x+=z
    return List

def count_by(x, n):
    return [i * x for i in range(1, n + 1)]

def count_by2(x, n):
    arr = []
    for num in range(1, n+1):
        result = x * num
        arr.append(result)
    return arr

# A=奇數, B=偶數=True 奇數=odd number, 偶數=even number
# A=奇數, B=奇數=False
def question2(f1,f2):
    if (f1%2==0 and f2%2==1) or (f1%2==1 and f2%2==0):
        return True
    else:
        return False

def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2==1

def lovefunc2(f1, f2):
    return True if (f1 % 2 == 0 and f2 % 2 != 0) or (f2 % 2 == 0 and f1 % 2 != 0) else False

def lovefunc3( flower1, flower2 ):
    return bool((flower1+flower2)%2)

def lovefunc4( flower1, flower2 ):
    if flower1%2 != flower2%2:
        return True
    else:
        return False

# 算平均值 input list. ex:[1,2,3] => avg=(1+2+3)/3=2
def question3(numbers):
    if len(numbers)>0:
        Sum=0
        for i in range(len(numbers)):
            Sum=Sum+numbers[i]
        return Sum/len(numbers)
    else:
        return 0

def find_average3(array):
    sum = 0
    for num in array:
        sum += num
    try:
        return sum/len(array)
    except ZeroDivisionError:
        return 0

def find_average(array):
    return sum(array) / len(array) if array else 0

def find_average2(array):
    if len(array) != 0:
        return sum(array) / len(array)
    else:
        return 0
        
# random sample
testdigit=random.sample(range(1,50), random.randint(1,5))
print(testdigit)

List=[]
for i in range(random.randint(1,5)):
    List.append(random.randint(1,50))
print(List)


if __name__=='__main__':
    # print(question1(1,10))
    # print(question1(2,5))
    # print(question2(1,2))
    # print(question2(2,2))
    # print(question3([1,2,3,4]))
    # print(question3([]))

    pass
