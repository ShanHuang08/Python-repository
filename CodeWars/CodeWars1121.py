# To be a senior, a member must be at least 55 years old and have a handicap greater than 7
# In this croquet club, handicaps range from -2 to +26;
input =  [(45, 12),(55,21),(19, -2),(104, 20)]
input2 =  [[45, 12],[55,21],[19, -2],[104, 20]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

# for x, y in input: #for loop解雙層列表
#     print(x, y)

def question1(input):
    output=[]
    for i in range(len(input)):
        if input[i][1] >= -2 and input[i][1] <= 26:
            if input[i][0] >= 55 and input[i][1] > 7:
                output.append("Senior")
            else:
                output.append("Open")
    print(output)
    return output

def openOrSenior2(data):
    res = []
    for i in data:
      if i[0] >= 55 and i[1] > 7:
        res.append("Senior")
      else:
        res.append("Open")
    return res

def openOrSenior(data): #best solution
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

def openOrSenior3(data):
    return["Senior" if (x[0] >= 55 and x[1] > 7) else "Open" for x in data]

# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. 
# Alternatively, if you rent the car for 3 or more days, you get $20 off your total.
# Write a code that gives out the total amount for different days(d).

def question2(Days):
    Total=Days*40
    if Days >= 3 and Days < 7:
        Total-=20
    if Days >= 7:
        Total-=50
    print(Total)
    return Total

def rental_car_cost(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30

def rental_car_cost2(d):
    discount = 50 if d > 6 else 20 if d > 2 else 0 
    return d * 40 - discount

# Break camelCase
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
Text="camelCasing"
# print(Text[5], Text[5].upper()) #i-1
def question3(Text):
    Space=[]
    NewText=''
    if len(Text) == 0:
        return ''
    for i in range(len(Text)):
        if Text[i] == Text[i].upper():
            Space.append(i-1)
    for j in range(len(Text)):
        NewText=NewText+Text[j]
        if j in Space:
            NewText=NewText+' '
    return NewText 

def solution(s): #Best
    return ''.join(' ' + c if c.isupper() else c for c in s)

def solution2(s):
    final_string = ""
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            final_string += " " + char
        else:
            final_string += char
    return final_string

def solution3(s): #2nd best
    newStr = ""
    for letter in s:
        if letter.isupper(): #大寫還沒有加上去
            newStr += " "
        newStr += letter
    return newStr

# print('v'.islower(), 'v'.isupper())

# 第一個大寫字母是分類
# M = {"A", "B", "C", "W"} 要從stocklist的分類資訊計算出M每個元素的值 (A : 20) - (B : 114) - (C : 50) - (W : 0)
# If L or M are empty return string is ""
# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python
# stocklist = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] #要分開
# Clist=["A", "B", "C", "W"]
stocklist = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
Clist=["A", "B", "C", "D"]
# stocklist = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
# Clist = ["A", "B"]

Category=[] #[['ABART', '20'], ['CDXEF', '50'], ['BKWRK', '25'], ['BTSQZ', '89'], ['DRTYM', '60']]
StockNum=[]
repeat=[]
for i in stocklist:
    List=i.split(' ')
    Category.append(List)
    StockNum.append(List[1])
    repeat.append(i[0])

repeatAmount=[]   
for item in repeat:
    freq=repeat.count(item)
    repeatAmount.append(freq)
Max=max(repeatAmount) #2 重複2次
  
sol=[]
for i in Clist:
    Sum=0
    for j in Category:
        if i == j[0][0]:
            Sum+=int(j[1])   
            sol.append('('+j[0][0]+' '+':'+' '+str(Sum)+')')
print(sol) #['(A : 20)', '(B : 25)', '(B : 114)', '(C : 50)']

Del=[]
DelCategory=''
RepeatLocation=[]
for j in range(len(sol)):
    for k in range(len(sol)):
        # print(sol[j][1])
        if sol[j][1] == sol[k][1]:
            Del.append(sol[j][1])
            RepeatLocation.append(j)
            # print(j)
for item in Del:
    freq=Del.count(item)
    if freq == Max*Max:
        DelCategory=item #B (重複出現) 

# 重複出現的如何從sol刪除 不能刪最後一個
# 把未包含的加回去
Delcount=1
print(RepeatLocation)
for i in sol:
    if i[1] == DelCategory and Delcount < Max:
        sol.pop()
        Delcount+=1
# print(sol)

# ['(A : 20)', '(B : 25)', '(B : 114)', '(C : 50)', '(D : 60)'] 
# 0 140行
# 1
# 1
# 2
# 2
# 3
# 4

# ['(B : 150)', '(B : 400)', '(B : 1290)', '(C : 515)', '(D : 600)']
# 0
# 0
# 0
# 1
# 1
# 1
# 2
# 2
# 2
# 3
# 4


if __name__=='__main__':
    # print(openOrSenior([(45, 12),(55,21),(19, -2),(104, 20)]))
    # print(rental_car_cost(7))
    # print(solution3("breakCamelCase"))

    pass