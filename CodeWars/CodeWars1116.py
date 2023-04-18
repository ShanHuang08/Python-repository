# 字串英文字母不重複 "Dermatoglyphics" --> true "aba" --> false "moOse" --> false ''-->True
def question1(string):
    answer=True
    for i in range(len(string)):
        for j in range(len(string)):
            if i != j:
                if string[i].lower() == string[j].lower():
                    answer=False
    print(answer)
    return answer

def question1_2(string):
    for i in range(len(string)):
        for j in range(len(string)):
            if i != j:
                if string[i].lower() == string[j].lower():
                    return False        
    return True

def is_isogram(string):
    return len(string) == len(set(string.lower())) #set 裡是不會包含重複的元素

def is_isogram2(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False #count() 方法用于统计字符串里某個字串或子字串出现的次数
    return True

is_isogram3=lambda s:len(s)==len(set(s.lower()))

# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")) # return "42 -9"
def question2(numbers):
    return ' '.join([str(max(int(numbers.split(' ')[i]) for i in range(len(numbers.split(' '))))), str(min(int(numbers.split(' ')[i]) for i in range(len(numbers.split(' ')))))])

def high_and_low4(num):
    return ' '.join((max(num.split(' '),key=int), min(num.split(' '),key=int)))

numbers="8 3 -5 42 -1 0 0 -9 4 7 4 -4"
def question2_2(numbers):
    List=numbers.split(' ')
    for i in range(len(List)):
        LargerDigit=[]
        SmallerDigit=[]
        for j in range(len(List)):
            if int(List[i]) < int(List[j]): #List[i]跟List[j]做比較，把比List[i]"大"的數字append到列表，看List[i]到哪一個數字，列表長度=0
                LargerDigit.append(List[j])
            elif int(List[i]) > int(List[j]): #List[i]跟List[j]做比較，把比List[i]"小"的數字append到列表，看List[i]到哪一個數字，列表長度=0
                SmallerDigit.append(List[j])
        if len(LargerDigit) == 0:
            MaxDigit=List[i]
        if len(SmallerDigit) == 0: 
            MinDigit=List[i]

    return ' '.join([MaxDigit, MinDigit])

def high_and_low5(numbers):
    numbers = numbers.split()

    min = max = int(numbers[0])

    for x in numbers:
        x = int(x)
        if x > max:
            max = x
        elif x < min:
            min = x

    
    return ' '.join([str(x) for x in (max, min)])


def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))


def high_and_low2(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])

def high_and_low3(numbers):
    numlist = numbers.split(" ")
    i = 0
    highest = int(numlist[0])
    lowest = int(numlist[0])
    while i < len(numlist):
        numlist[i] = int(numlist[i])
        if numlist[i] > highest:
            highest = numlist[i]
        if numlist[i] < lowest:
            lowest = numlist[i]
        i += 1
    highest = str(highest)
    lowest = str(lowest)
    return  highest+" "+lowest

if __name__=='__main__':
    # question1('Dermatoglyphics')
    # question1('wkuxdDphn')
    # print(is_isogram('Dermatoglyphics'))
    # print(is_isogram('wkuxdDphn'))
    # print(is_isogram2('Dermatoglyphics'))
    # print(is_isogram2('wkuxdDphn'))
    # print(question2("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
    # print(question2_2("2 1 3"))
    # print(question2_2("3 2 1"))
    # print(question2_2("1 2 3"))
    pass