from random import choice, randint
al='abcdefghijklmnopqrstuvwxyz'
digit='1234567890'
def KeyGenerator():

    result=''
    for i in range(2):
        List=[]
        for i in range(3):
            TextList=[
                choice(al.upper())+choice(digit)+choice(al),
                choice(al)+choice(digit)+choice(al.upper()),
                choice(digit)+choice(al.upper())+choice(al)]
            List.append(TextList[randint(0,2)])
        # print(List)
        for j in List:
            result+=j
        result=result+'\n'
    return result

def AI_Optimize():
    result = ''
    for i in range(2):
        sub_result = ''.join([f'{choice(al.upper())}{choice(digit)}{choice(al)}' for k in range(3)])
        result += f'{sub_result}\n'
    return result


def StringGenerator():
    digit = int(input("字串長度: "))
    result = ''
    for i in range(digit):
        result+=choice(al)
    print(result)
        


if __name__=='__main__':
    # print(KeyGenerator())
    StringGenerator()

