def main(words): #My answer
    if len(words)==0: 
        return ""
    elif len(words)>0:
        answer=' '.join(words)
    return answer

def smash(words):
    # Begin here
    result = ""
    for i in range(len(words)):
        if i != len(words)-1: #如果不是最後一位
            result = result + words[i] + " "
        else:
            result = result + words[i]
    return result

def smash4(words):
    concat = ''
    for i in range (len(words)):
        if (i == 0):
            concat = words[i]
        else:
            concat = concat + ' ' + words[i]
    return concat   

def smash2(words):
    sen = ""
    for x in words :
        sen += x +" "
    return sen[0:len(sen)-1] 

def smash3(words):
    sen_words =""
    for wd in words:
        sen_words += " " + wd
        
    return sen_words.lstrip()


if __name__=='__main__':
    # print(main([""]))
    # print(main(["hello"]))
    # print(main(["hello", "world"]))
    print(smash([""]))
    print(smash(["hello"]))
    print(smash(["hello", "world"]))
    print(smash2([""]))
    print(smash2(["hello"]))
    print(smash2(["hello", "world"]))
    print(smash3([""]))
    print(smash3(["hello"]))
    print(smash3(["hello", "world"]))
    print(smash4([""]))
    print(smash4(["hello"]))
    print(smash4(["hello", "world"]))
