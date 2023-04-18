import os
def CountByDict():
    string = input("請輸入字串: ") #test
    char_dict = {}

    # 計算字元出現次數
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    # print(char_dict) {'t': 2, 'e': 1, 's': 1}
    # 加總字元出現次數
    total = 0
    for count in char_dict.values(): #把dict的值加總
        total += count
    return total

def CountByStr():
    string = input("請輸入字串: ")
    return len(string)

if __name__=='__main__':
    # print(CountByDict())
    print(CountByStr())