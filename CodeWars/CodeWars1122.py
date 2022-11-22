# 第一個大寫字母是分類
# M = {"A", "B", "C", "W"} 要從stocklist的分類資訊計算出M每個元素的值 (A : 20) - (B : 114) - (C : 50) - (W : 0)
# If L or M are empty return string is ""

def bookseller(stocklist, Clist):
    print(stocklist)
    if stocklist == [] or Clist ==[]:
        return ""

    if stocklist != [] or Clist != []:
        Category=[] #[['ABART', '20'], ['CDXEF', '50'], ['BKWRK', '25'], ['BTSQZ', '89'], ['DRTYM', '60']]
        StockNum=[]
        repeat=[] #['B', 'C', 'B', 'B', 'D']

        for i in stocklist:
            List=i.split(' ')
            Category.append(List)
            StockNum.append(List[1])
            repeat.append(i[0])
        # print(f'repeat= {repeat}')
        repeatAmount=[]   
        for item in repeat:
            freq=repeat.count(item)
            repeatAmount.append(freq)
        Max=max(repeatAmount) #2 重複2次
        # print(f'repeatAmount= {repeatAmount}')
        # print(f'Max= {Max}')
        
        sol=[]
        for i in Clist:
            Sum=0
            for j in Category:
                if i == j[0][0]:
                    Sum+=int(j[1])   
                    sol.append('('+j[0][0]+' '+':'+' '+str(Sum)+')')
        # print(sol) #['(B : 25)', '(B : 114)', '(C : 20)', '(C : 70)']

        Del=[]
        DelCategory=''
        RepeatLocation=[]
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
            # print(DelCategory) #B跟C都是4
        # print(f'DelCategory= {DelCategory}') #印C
        Firstele=[]
        for i in range(len(RepeatLocation)):
            if RepeatLocation.count(RepeatLocation[i]) > 1:
                Firstele.append(i)
        First=Firstele[0] #要刪除的位置
        # print(f'Firstele= {Firstele}')
        # print(f'First= {First}')

        Delcount=1 #因為最後一個不能刪除
        for k in sol:
            # print(k) #0,2,4 第0個被remove, 第1個變第0個 所以直接跳第2個
            if k[1] == DelCategory and Delcount < Max:
                # print(f'remove= {k}') 
                sol.pop(First)
                if k[1] != sol[First][1]: 
                    sol.pop(First+(Max-1)) #First=0 刪第0個 (B : 25)被刪掉
                Delcount+=1

        # 把未包含的加回去
        for i in Clist:
            if i not in repeat:
                sol.append('('+i+' '+':'+' '+'0'+')')
        sol.sort() #遞增之後，sort的順序可能會跟Clist不一樣
        # print(sol)
        sol2=[]
        for i in range(len(Clist)):
            for j in range(len(sol)):
                if Clist[i] == sol[j][1]:
                    sol2.append(sol[j])
        # print(sol)
        # print(sol2)
        answer=''
        for i in range(len(sol2)):
            if i != len(sol2)-1:
                answer+=sol2[i]+' - '
            else:
                answer+=sol2[i]
        print(answer)
        return answer

if __name__=='__main__':
    stocklist = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] #要分開
    Clist=["A", "B", "C", "W"] #(A : 20) - (B : 114) - (C : 50) - (W : 0)
    stocklist2 = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    Clist2=["A", "B", "C", "D"] #(A : 0) - (B : 1290) - (C : 515) - (D : 600)
    stocklist3 = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    Clist3 = ["A", "B"] #(A : 200) - (B : 1140)
    stocklist4 = ['CBART 20', 'CDXEF 50', 'BKWRK 25', 'BTSQZ 89', 'DRTYM 60']
    Clist4 = ["A", "B", "C", "W"] #(A : 0) - (B : 114) - (C : 70) - (W : 0)
    stocklist5 = ['ROXANNE 102', 'RHODODE 123', 'BKWRKAA 125', 'BTSQZFG 239', 'DRTYMKH 060']
    Clist5 = ["B", "R", "D", "X"] #(B : 364) - (R : 225) - (D : 60) - (X : 0)
    stocklist6 = []
    Clist6= ['B', 'R', 'D', 'X'] #[]
    bookseller(stocklist, Clist)
    bookseller(stocklist2, Clist2)
    bookseller(stocklist3, Clist3)
    bookseller(stocklist4, Clist4)
    bookseller(stocklist5, Clist5)
    bookseller(stocklist6, Clist6)