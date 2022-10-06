import unittest
from Employee import EmployeeData

class TestEmployee(unittest.TestCase):
    def test_fullname(self):
        emp1=EmployeeData('Laibah','Borys',30000)
        emp2=EmployeeData('Zarah','Clegg',50000)
        self.assertEqual(emp1.fullname,'Laibah Borys')
        self.assertEqual(emp2.fullname,'Zarah Clegg')

    def test_email(self):
        emp1=EmployeeData('Laibah','Borys',30000)
        emp2=EmployeeData('Zarah','Clegg',50000)
        self.assertEqual(emp1.email,'Laibah.Borys@email.com')
        self.assertEqual(emp2.email,'Zarah.Clegg@email.com')

    def test_wage(self):
        emp1=EmployeeData('Laibah','Borys',30000)
        emp2=EmployeeData('Zarah','Clegg',50000)
        self.assertEqual(emp1.wage,30000)
        self.assertEqual(emp2.wage,50000)

    def test_wageraise(self):
        emp1=EmployeeData('Laibah','Borys',30000)
        emp2=EmployeeData('Zarah','Clegg',50000)
        self.assertEqual(emp1.wageraise,31500)
        self.assertEqual(emp2.wageraise,52500)




if __name__=='__main__':
    unittest.main()