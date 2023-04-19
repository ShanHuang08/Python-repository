<<<<<<< HEAD
import unittest
def Text_transitionBy_List(Text):
    AlList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    TextList=[]
    for i in range(len(Text)):
        for j in range(len(AlList)):
            if Text[i].lower() == AlList[j]:
                TextList.append(str(j+1))        
    answer=''
    for k in range(len(TextList)):
        if k == len(TextList)-1:
            answer+=TextList[k]
        else:
            answer+=TextList[k]+','
    return answer

def Text_transitionBy_String(Text):
    Alstr='abcdefghijklmnopqrstuvwxyz'
    answer=''
    for i in range(len(Text)):
        for j in range(len(Alstr)):
            if i == len(Text)-1 and Text[i].lower() == Alstr[j]:
                answer+=str(j+1)
            elif Text[i].lower() == Alstr[j]:
                answer+=str(j+1)+','  
    return answer

class testcases(unittest.TestCase):
    def test_Basic_Test(self):
        self.assertEqual(Text_transitionBy_List('FDrgr'), '6,4,18,7,18')
        self.assertEqual(Text_transitionBy_String('FDrgr'), '6,4,18,7,18')


if __name__=='__main__':
    unittest.main()
=======
import unittest
def Text_transitionBy_List(Text):
    AlList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    TextList=[]
    for i in range(len(Text)):
        for j in range(len(AlList)):
            if Text[i].lower() == AlList[j]:
                TextList.append(str(j+1))        
    answer=''
    for k in range(len(TextList)):
        if k == len(TextList)-1:
            answer+=TextList[k]
        else:
            answer+=TextList[k]+','
    return answer

def Text_transitionBy_String(Text):
    Alstr='abcdefghijklmnopqrstuvwxyz'
    answer=''
    for i in range(len(Text)):
        for j in range(len(Alstr)):
            if i == len(Text)-1 and Text[i].lower() == Alstr[j]:
                answer+=str(j+1)
            elif Text[i].lower() == Alstr[j]:
                answer+=str(j+1)+','  
    return answer

class testcases(unittest.TestCase):
    def test_Basic_Test(self):
        self.assertEqual(Text_transitionBy_List('FDrgr'), '6,4,18,7,18')
        self.assertEqual(Text_transitionBy_String('FDrgr'), '6,4,18,7,18')


if __name__=='__main__':
    unittest.main()
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
