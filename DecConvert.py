

def BinConvert(num):
    if type(num)==int:
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
    elif type(num)==bool:
        if num==True:
            return 1
        else:
            return 0
    elif type(num)==str:
        return 'Not support str, please input int'
    else:
        return 'Input error'

def BintoDec(init_num):
    if type(init_num)==int:
        num=str(init_num)
    elif type(init_num)==str:
        num=init_num   
    else:
        return 'Type error, only support str and int' 

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
    
    





def test():
    Dec=100
    Bin=BinConvert(Dec)
    print(BinConvert(Dec))
    print(BintoDec(Bin))

test()

