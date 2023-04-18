

def BinConvert(num):
    if type(num)==int:
        num=num
    elif type(num)==str:
        num=int(num)
    elif type(num)==bool:
        if num==True:
            return 1
        else:
            return 0
    else:
        return 'Input error'
    List=[]
    if num>0:
        while num>=1:
            res=num%2
            num=num//2
            # List.insert(-1,str(res))
            List.append(str(res))
        List.reverse()
        sres=''.join(List)
        return sres
    elif num==0:
        return 0
    else:
        num2=abs(num)
        while num2>=1:
            res2=num2%2
            num2=num2//2
            List.append(str(res2))
        List.reverse()
        sres2=''.join(List)
        return '-'+sres2


def BintoDec(init_num):
    if type(init_num)==int:
        num=str(init_num)
    elif type(init_num)==str:
        num=init_num   
    else:
        raise TypeError('Type error, only support str and int') 
    
    for i in range(len(num)):
        if num[i] not in ['0','1']:
            raise ValueError('num must include 0 and 1')


    List=[]
    for i in range(len(num)-1,-1,-1):
        List.append(num[i])
    res=''.join(List)
    # print(len(res))=3 '001'
    x=0
    num2=0
    sum=0
    while x<len(res):
        if res[x]=='1':
            num2=2**x
        elif res[x]=='0':
            num2=0
        sum=sum+num2
        x+=1
    # print(sum)
    return sum
    
    





if __name__=='__main__':
    Dec=100
    Bin=BinConvert(Dec)
    print(BinConvert(Dec))
    print(BintoDec(Bin))



