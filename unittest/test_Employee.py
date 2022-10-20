import unittest
from Employee import EmployeeData

class TestEmployee(unittest.TestCase):
    def setUp(self) -> None: #setUp最先執行
        self.emp1=EmployeeData('Laibah','Borys',30000)
        self.emp2=EmployeeData('Zarah','Clegg',50000)
        # print('setUp最先執行')

    def tearDown(self) -> None: #tearDown最後執行
        pass
        # print('tearDown最後執行')
    
    def test_fullname(self):
        self.assertEqual(self.emp1.fullname,'Laibah Borys')
        self.assertEqual(self.emp2.fullname,'Zarah Clegg')

        self.emp1.last='Corse'
        self.emp2.last='chen'
        self.assertEqual(self.emp1.fullname,'Laibah Corse')
        self.assertEqual(self.emp2.fullname,'Zarah chen')

    def test_email(self):
        self.assertEqual(self.emp1.email,'Laibah.Borys@email.com')
        self.assertEqual(self.emp2.email,'Zarah.Clegg@email.com')

        self.emp1.first='John'
        self.emp2.first='stepe'
        self.assertEqual(self.emp1.email, 'John.Borys@email.com')
        self.assertEqual(self.emp2.email,'stepe.Clegg@email.com')

    def test_wage(self):
        self.assertEqual(self.emp1.wage,30000)
        self.assertEqual(self.emp2.wage,50000)

    def test_wageraise(self):
        self.assertEqual(self.emp1.wageraise,31500)
        self.assertEqual(self.emp2.wageraise,52500)

if __name__=='__main__':
    unittest.main()