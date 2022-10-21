import unittest
import calc
from Employee import EmployeeData

class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.args=(2,3)
        self.args2=(2,4)
        # self.args=(3,3)
        self.emp1=EmployeeData('Laibah','Borys',30000)
        self.emp2=EmployeeData('Zarah','Clegg',50000)

    def tearDown(self) -> None:
        self.args=None

    def test_add(self):
        expected=5
        result=calc.add(*self.args)
        self.assertEqual(result,expected)
        self.assertEqual(expected,result)
        
    def test_add2(self):
        expected=5
        result=calc.add(2,3)
        self.assertEqual(result,expected)
        self.assertEqual(expected,calc.add(2,3)) #兩個都可以
        

    def test_substract(self):
        result=calc.substract(*self.args)
        self.assertEqual(result,-1)
        self.assertEqual(-1,result)
        self.assertEqual(calc.substract(*self.args2),-2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(*self.args),6)
        self.assertEqual(calc.multiply(*self.args2),8)
        self.assertEqual(calc.multiply(10,5),50)
        self.assertRaises(ValueError,calc.multiply,10,0)
        with self.assertRaises(ValueError):
            self.assertRaises(calc.multiply(10,0),0)

    def test_division(self):
        self.assertEqual(calc.division(*self.args),0.6666666666666666)
        self.assertEqual(calc.division(*self.args2),0.5)
        self.assertEqual(calc.division(10,5),2)
        self.assertRaises(ValueError,calc.division,10,0)
        with self.assertRaises(ValueError):
            self.assertRaises(calc.division(10,0),0)
        


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
        self.assertEqual(self.emp1.email,'John.Borys@email.com')
        self.assertEqual(self.emp2.email,'stepe.Clegg@email.com')

    def test_wage(self):
        self.assertEqual(self.emp1.wage,30000)
        self.assertEqual(self.emp2.wage,50000)

    def test_wageraise(self):
        self.assertEqual(self.emp1.wageraise,31500)
        self.assertEqual(self.emp2.wageraise,52500)


if __name__=='__main__':
    unittest.main()