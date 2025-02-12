def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    if x==0 or y==0:
        raise ValueError("Can't multiply zero")
    return x*y
def division(x,y):
    if x==0 or y==0:
        raise ValueError("Can't divided by zero")
    return x/y
def power(x,y):
    return x**y

class calculator():
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    @property
    def add(self):
        return self.x+self.y
    @property
    def substract(self):
        return self.x-self.y
    @property
    def multiply(self):
        if self.x==0 or self.y==0:
            raise ValueError("Can't multiply zero") 
        return self.x*self.y
    @property
    def divided(self):
        if self.x==0 or self.y==0:
            raise ValueError("Can't divided by zero") 
        return self.x/self.y
    @property
    def power(self):
        if self.x==0 or self.y==0:
            raise ValueError
        return self.x**self.y