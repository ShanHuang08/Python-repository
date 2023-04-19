<<<<<<< HEAD
# NeedDefined=','.join([str(x),str(y)]) #x,y需要先定義 NameError: name 'x' is not defined
NoDefined=lambda x,y:','.join([str(x),str(y)]) #x,y不需要先定義, 直接輸入參數
print(NoDefined(9,10))
print((lambda x,y:' ~ '.join([str(x),str(y)]))(99,98))


def test(x,y):
    test=lambda x,y:','.join([str(x),str(y)]) #x,y不需要先定義
    return test(x,y)

def test2(x,y):
    test2=','.join([str(x),str(y)]) #x,y需要先定義
    return test2

def lam_add(x,y):
    return (lambda x,y: x + y)(x,y)

def add(x,y):
    return x+y

if __name__=='__main__':
    print(test(2,3))
    print(test2(2,3))
    print(lam_add(2,3))
    print(add(2,3))
    # (lambda parameter: expression)(argument)
    # print((lambda x,y: x + y)(4,5))
=======
# NeedDefined=','.join([str(x),str(y)]) #x,y需要先定義 NameError: name 'x' is not defined
NoDefined=lambda x,y:','.join([str(x),str(y)]) #x,y不需要先定義, 直接輸入參數
print(NoDefined(9,10))
print((lambda x,y:' ~ '.join([str(x),str(y)]))(99,98))


def test(x,y):
    test=lambda x,y:','.join([str(x),str(y)]) #x,y不需要先定義
    return test(x,y)

def test2(x,y):
    test2=','.join([str(x),str(y)]) #x,y需要先定義
    return test2

def lam_add(x,y):
    return (lambda x,y: x + y)(x,y)

def add(x,y):
    return x+y

if __name__=='__main__':
    print(test(2,3))
    print(test2(2,3))
    print(lam_add(2,3))
    print(add(2,3))
    # (lambda parameter: expression)(argument)
    # print((lambda x,y: x + y)(4,5))
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
    pass