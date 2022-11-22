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


if __name__=='__main__':
    # print(openOrSenior([(45, 12),(55,21),(19, -2),(104, 20)]))
    # print(rental_car_cost(7))
    # print(solution3("breakCamelCase"))

    pass