<<<<<<< HEAD

class EmployeeData():
    raise_am=1.05

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    
    @property
    # 沒有寫property會出現 AssertionError: <bound method EmployeeData.fullname of <E[46 chars]420>> != 'Laibah Borys'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def wage(self):
        return int(self.pay)
    @property
    def wageraise(self):
=======

class EmployeeData():
    raise_am=1.05

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    
    @property
    # 沒有寫property會出現 AssertionError: <bound method EmployeeData.fullname of <E[46 chars]420>> != 'Laibah Borys'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def wage(self):
        return int(self.pay)
    @property
    def wageraise(self):
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
        return int(self.pay*self.raise_am)