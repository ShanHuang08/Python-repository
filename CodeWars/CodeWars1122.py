from collections import Counter
# 第一個大寫字母是分類
# stocklist = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
# M = {"A", "B", "C", "W"} 要從stocklist的分類資訊計算出M每個元素的值 (A : 20) - (B : 114) - (C : 50) - (W : 0)
# If L or M are empty return string is ""

def bookseller(stocklist, Clist):
    # print(stocklist)
    if stocklist == [] or Clist ==[]:
        return ""

    if stocklist != [] or Clist != []:
        # 用split()把代號跟數量分開
        Category=[] #[['ABART', '20'], ['CDXEF', '50'], ['BKWRK', '25'], ['BTSQZ', '89'], ['DRTYM', '60']]
        FirstWord=[] #['A', 'C', 'B', 'B', 'D']

        for i in stocklist:
            List=i.split(' ')
            Category.append(List)
            FirstWord.append(i[0]) #取第一個字母

        repeatAmount=[] #[1, 1, 2, 2, 1]   
        for item in FirstWord:
            freq=FirstWord.count(item)
            repeatAmount.append(freq)
        Max=max(repeatAmount) #2 重複2次
        # print(f'repeatAmount= {repeatAmount}')
        # print(f'Max= {Max}')
        
        sol=[] #['(A : 20)', '(B : 25)', '(B : 114)', '(C : 50)']
        for i in Clist:
            Sum=0
            for j in Category:
                if i == j[0][0]:
                    Sum+=int(j[1])   
                    sol.append('('+j[0][0]+' '+':'+' '+str(Sum)+')')
        # print(sol) 

        # 找出重複的元素
        Del=[] #['A', 'B', 'B', 'B', 'B', 'C']
        DelCategory='' #B
        RepeatLocation=[] #[0, 1, 1, 2, 2, 3]
        for j in range(len(sol)):
            for k in range(len(sol)):
                # print(sol[j][1])
                if sol[j][1] == sol[k][1]:
                    Del.append(sol[j][1])
                    RepeatLocation.append(j)
                    # print(j)

        for item in Del:
            freq=Del.count(item)
            # print(f'freq= {freq}') #8個4
            if freq == Max*Max:
                DelCategory=item # 重複出現

        # 定位開始重複的位置
        Firstele=[] #[1, 2, 3, 4]
        for i in range(len(RepeatLocation)):
            if RepeatLocation.count(RepeatLocation[i]) > 1:
                Firstele.append(i)
        First=Firstele[0] #要刪除的位置
        # print(f'Firstele= {Firstele}')
        # print(f'First= {First}')

        # 刪除重複elements
        Delcount=1 #因為最後一個不能刪除
        for k in sol:
            # print(k) #0,2,4 第0個被remove, 第1個變第0個 所以直接跳第2個
            if k[1] == DelCategory and Delcount < Max: #k[1] == B
                # print(f'sol[First][1]= {sol[First][1]}') 
                sol.pop(First) #0
                if k[1] != sol[First][1]: #sol[First][1]= B
                    sol.pop(First+(Max-1)) # 0+(2-1)
                Delcount+=1

        # 把未包含的加回去
        for i in Clist:
            if i not in FirstWord:
                sol.append('('+i+' '+':'+' '+'0'+')')
        sol.sort() #遞增之後，sort的順序可能會跟Clist不一樣
        # print(sol)
        sol2=[] #['(A : 20)', '(B : 114)', '(C : 50)', '(W : 0)']
        for i in range(len(Clist)):
            for j in range(len(sol)):
                if Clist[i] == sol[j][1]:
                    sol2.append(sol[j])

        answer=''
        for i in range(len(sol2)):
            if i != len(sol2)-1:
                answer+=sol2[i]+' - '
            else:
                answer+=sol2[i]
        print(answer)
        return answer

def stock_list(listOfArt, listOfCat):
    if (len(listOfArt) == 0) or (len(listOfCat) == 0):
        return ""
    result = ""
    for cat in listOfCat:
        total = 0
        for book in listOfArt:
            if (book[0] == cat[0]):
                total += int(book.split(" ")[1])
        if (len(result) != 0):
            result += " - "
        result += "(" + str(cat) + " : " + str(total) + ")"
    print(result)
    return result

def stock_list2(listOfArt, listOfCat):
    if not listOfArt:
        return ''
    codePos = listOfArt[0].index(' ') + 1
    cnt = Counter()
    for s in listOfArt:
        cnt[s[0]] += int(s[codePos:])
    return ' - '.join('({} : {})'.format(cat, cnt[cat]) for cat in listOfCat)

def stock_list3(listOfArt, listOfCat):
    # Split the query by alphabet and numeric for easy processing
    new = [x.split(' ') for x in listOfArt]
    
    # Create keys with value of 0 from listOfCat to track the category totals
    d = {x : 0 for x in listOfCat}
    
    # totals list is created to append answers in string format to get proper formatting on answer
    totals = []
    
    # Determin if critera is met
    if len(listOfArt) > 0:
        
        # Iterate through the new split list grabbing the first character of the alphabetic value check if it is in d dict
        for x, y in new:
            if x[0] in d:
                # Convert the numeric value into int and add it to the corresponding key values in d dict
                d[x[0]] += int(y)    
        
        # Iterate through the dictionary to grab the key / item and append it to totals      
        for a, b in d.items():
            totals.append(f'({a} : {b})')
            
    # If critera not met return empty empty string
    else:
        return ''
    
    # Join the totals list to generate proper formatting for resonse
    return (' - ').join(totals)

if __name__=='__main__':
    stocklist = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] #要分開
    Clist=["A", "B", "C", "W"] #(A : 20) - (B : 114) - (C : 50) - (W : 0)
    listOfArt = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] #要分開
    listOfCat=["A", "B", "C", "W"] #(A : 20) - (B : 114) - (C : 50) - (W : 0)
    # stocklist2 = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    # Clist2=["A", "B", "C", "D"] #(A : 0) - (B : 1290) - (C : 515) - (D : 600)
    # stocklist3 = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    # Clist3 = ["A", "B"] #(A : 200) - (B : 1140)
    # stocklist4 = ['CBART 20', 'CDXEF 50', 'BKWRK 25', 'BTSQZ 89', 'DRTYM 60']
    # Clist4 = ["A", "B", "C", "W"] #(A : 0) - (B : 114) - (C : 70) - (W : 0)
    # stocklist5 = ['ROXANNE 102', 'RHODODE 123', 'BKWRKAA 125', 'BTSQZFG 239', 'DRTYMKH 060']
    # Clist5 = ["B", "R", "D", "X"] #(B : 364) - (R : 225) - (D : 60) - (X : 0)
    # stocklist6 = []
    # Clist6= ['B', 'R', 'D', 'X'] #[]
    bookseller(stocklist, Clist)
    stock_list(listOfArt, listOfCat)
