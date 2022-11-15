# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaced  words"      ==> "elbuod  decaps  sdrow"
def question1(text):  #難
    rtext=''
    Lengths=[]
    List=text.split(' ')
    
    for k in range(len(List)): #把List之內的字串長度append到 Lengths列表
        Lengths.append(len(List[k]))

    if min(Lengths) == 0: #判斷空格長度
        Space='  '
    else:
        Space=' '
            
    for i in range(len(List)):
        for j in range(len(List[i])-1,-1,-1): #用雙for loop顛倒List裡面的字串
            if j == 0 and i != len(List)-1 and len(List[i]) != 0: #假如j=0 and 不是最後一個字串 and 字串長度不是0, 後面加空格
                rtext=rtext+List[i][j]+Space 
            else:
                rtext=rtext+List[i][j]
    return rtext

def question1_2(text): #better
    rtext=''
    for i in range(len(text)-1,-1,-1): #將全部字串反轉
        rtext=rtext+text[i]

    List=rtext.split(' ') #將字串變成列表
    answer=''
    for j in range(len(List)-1,-1,-1): #把列表反向
        answer=answer+List[j]+' '
    return answer


def reverse_words(str):
  #go for it
    newStr = []
    for i in str.split(' '):
        print(i[::-1]) #倒序 一個一個列
        newStr.append(i[::-1])
    print(newStr)
    return ' '.join(newStr)


def reverse_words2(str):
    return ' '.join(s[::-1] for s in str.split(' '))

def reverse_words3(string): 
    string = string[::-1] 
    word_r = string.split(' ')
    word_r.reverse()
    output = ' '.join(word_r)
    return output

if __name__=='__main__':
    # print(question1("This is an example!"))
    # print(question1("double  spaced  words"))
    # print(reverse_words("This is an example!"))
    print(reverse_words("double  spaced  words"))
    # print(reverse_words2("This is an example!"))
    # print(reverse_words2("double  spaced  words"))

