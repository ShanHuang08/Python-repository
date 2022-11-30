def stock_list(listOfArt, listOfCat):
    if (len(listOfArt) == 0) or (len(listOfCat) == 0):
        return ""
    Category=[]
    for i in listOfArt:
        List=i.split(' ')
        Category.append(List)

    dic={i : 0 for i in listOfCat}
    # print(dic) #{'A': 0, 'B': 0, 'C': 0, 'W': 0}
    for i in Category:
        if i[0][0] in dic:
            dic[i[0][0]]+=int(i[1])
    result=[]
    for j in dic.items():
        result.append('('+j[0]+' : '+str(j[1])+')')
    answer=' - '.join(result)
    print(answer)
    return answer

def stock_list2(listOfArt, listOfCat):
    Category=[i.split() for i in listOfArt]
    dic={x:0 for x in listOfCat}
    for i,j in Category:
        # print(i[0],j)
        if i[0] in dic:
            dic[i[0]]+=int(j)
    result=[]
    for i,j in dic.items():
        # print(i,j)
        result.append('('+i+' : '+str(j)+')')
    answer=' - '.join(result)
    print(answer)
    return answer

if __name__=='__main__':
    listOfArt = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] #要分開
    listOfCat=["A", "B", "C", "W"] #(A : 20) - (B : 114) - (C : 50) - (W : 0)
    stock_list(listOfArt, listOfCat)
    stock_list2(listOfArt, listOfCat)