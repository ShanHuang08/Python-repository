<<<<<<< HEAD
import unittest
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

class testcases(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(main([]), '')
        self.assertEqual(smash2([]), '')

    def test_Single_word(self):
        self.assertEqual(main(["hello"]), 'hello')
        self.assertEqual(smash(["hello"]), 'hello')
    
    def test_Two_words(self):
        self.assertEqual(smash3(["hello", "world"]), 'hello world')
        self.assertEqual(smash4(["hello", "world"]), 'hello world')


if __name__=='__main__':
    unittest.main()
=======
import unittest
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

class testcases(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(main([]), '')
        self.assertEqual(smash2([]), '')

    def test_Single_word(self):
        self.assertEqual(main(["hello"]), 'hello')
        self.assertEqual(smash(["hello"]), 'hello')
    
    def test_Two_words(self):
        self.assertEqual(smash3(["hello", "world"]), 'hello world')
        self.assertEqual(smash4(["hello", "world"]), 'hello world')


if __name__=='__main__':
    unittest.main()
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
