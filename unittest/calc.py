def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if x==0 or y==0:
        raise ValueError("Can't divided by zero")
    return x/y
def power(x,y):
    return x**y