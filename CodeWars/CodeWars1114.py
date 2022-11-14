def question3(a,b):
    List=[]
    Sum=a+b
    while Sum > 0: 
        List.append(Sum%2)
        Sum=Sum // 2 
    answer=''
    for i in range(len(List)-1,-1,-1):
        answer=answer+str(List[i])
    return answer

def add_binary(a,b):
    return bin(a+b)[2:]

def add_binary2(a,b):
    return '{0:b}'.format(a + b)

def add_binary3(a, b):
    return format(a + b, 'b')

if __name__=='__main__':
    print(add_binary3(6,8))