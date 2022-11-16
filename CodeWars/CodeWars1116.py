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

numbers="8 3 -5 42 -1 0 0 -9 4 7 4 -4"





if __name__=='__main__':
    # question1('Dermatoglyphics')
    # question1('wkuxdDphn')
    # print(is_isogram('Dermatoglyphics'))
    # print(is_isogram('wkuxdDphn'))
    # print(is_isogram2('Dermatoglyphics'))
    # print(is_isogram2('wkuxdDphn'))
   
    pass