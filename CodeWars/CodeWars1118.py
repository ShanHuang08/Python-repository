# n=5
# for i in range(n+1):
#         print(''*(n-i)+'*'*i)
# 1 -->  1
# 2 --> 3 + 5 = 8
# 3 --> 7 + 9 + 11 =27

def question1(n):
    Digit=1
    Sum=0
    for i in range(n+1):
        if i == 1: #1
            print('   '*(n-i)+str(Digit)*i) #f1

            Digit+=2
        if i == n == 1:
            Sum=Digit
               
        if i > 1:
            for j in range(i):
                if i == n:
                    Sum+=Digit
                if j == 0:
                    print('   '*(n-i)+(str(Digit))+'  ',end='') #i=2 Digit加2次 #每一行的開頭 #f2
                elif i == 3 and j == 2: #11要用<10的公式
                    print('   '+(str(Digit))+'  ',end='') #f3
                elif j > 0 and Digit < 10:
                    print('   '+(str(Digit))+'  ',end='') #f3
                elif j > 0 and Digit >= 10:
                    print('  '+(str(Digit))+'  ',end='') #f4
                Digit+=2 
            print()
    return Sum

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def question2(n):
    num1=''
    num2=''
    num3=''
    for i in n[0:3]:
        num1=num1+str(i)
    for j in n[3:6]:
        num2=num2+str(j)
    for k in n[6:10]:
        num3=num3+str(k)
    return '('+num1+') '+num2+'-'+num3

def create_phone_number(n):
    number='('
    for i in range(0,3):
        number=number+str(n[i])
    number=number+')'+' '
    for j in range(3,6):
        number=number+str(n[j])
    number=number+'-'
    for t in range(6,10):
        number=number+str(n[t])
    return number

def create_phone_number2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number2_2(n1,n2,n3,n4,n5,n6,n7,n8,n9,n0):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(n1,n2,n3,n4,n5,n6,n7,n8,n9,n0)

def create_phone_number3(n):
    str1 =  ''.join(str(x) for x in n[0:3])
    str2 =  ''.join(str(x) for x in n[3:6])
    str3 =  ''.join(str(x) for x in n[6:10])
    return '({}) {}-{}'.format(str1, str2, str3)

if __name__=='__main__':
    # print(question1(4))
    print(create_phone_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(create_phone_number2_2('1','2','3','4','5','6','7','8','9','0'))
    pass