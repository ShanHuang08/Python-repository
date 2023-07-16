import unittest
# stocklist = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
# Clist= ['B', 'R', 'D', 'X']
def stock_list(stocklist, Clist):
    if (stocklist == []) or (Clist == []):
        return ""
    Category=[]
    for i in stocklist:
        List=i.split(' ')
        Category.append(List)
    # print(Category[0][0])
    sol=[]
    for i in Clist:
        Sum=0
        for j in Category:
            if i == j[0][0]:
                Sum+=int(j[1])
                # print(i) # i會在j的迴圈跑兩次 所以用i也會出現2個B
            # print(j[0][0])
                # sol.append('('+j[0][0]+' '+':'+' '+str(Sum)+')') #['(B : 25)', '(B : 114)', '(D : 60)']
        sol.append('('+i+' '+':'+' '+str(Sum)+')') #['(B : 114)', '(R : 0)', '(D : 60)', '(X : 0)']
        # sol.append('('+j[0][0]+' '+':'+' '+str(Sum)+')') #['(D : 114)', '(D : 0)', '(D : 60)', '(D : 0)'] Category的最後一個是D!

    answer=''
    for i in range(len(sol)):
        if i != len(sol)-1:
            answer+=sol[i]+' - '
        else:
            answer+=sol[i]
    # print(answer)
    return answer

class Testcase(unittest.TestCase):
    def test_BasicTest(self):
        stocklist = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
        Clist= ['B', 'R', 'D', 'X']
        self.assertEqual(stock_list(stocklist, Clist), '(B : 114) - (R : 0) - (D : 60) - (X : 0)')

if __name__=='__main__':
    stocklist = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
    Clist= ['B', 'R', 'D', 'X']
    stock_list(stocklist, Clist)
    # unittest.main()
