from cgitb import reset
import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result=calc.add(10,5)
        self.assertEqual(result,15)
        self.assertEqual(calc.add(10,26),36)

    def test_substract(self):
        result=calc.substract(10,5)
        self.assertEqual(result,5)
        self.assertEqual(calc.substract(10,16),-6)

    def test_multiply(self):
        result=calc.multiply(10,5)
        self.assertEqual(result,50)
        self.assertEqual(calc.multiply(10,2),20)

    def test_power(self):
        self.assertEqual(calc.power(10,2),100)
        self.assertEqual(calc.power(1,0),1)    

    def test_division(self):
        result=calc.division(10,5)
        self.assertEqual(result,2.0)
        self.assertEqual(calc.division(1,1),1)

if __name__=='__main__':
    unittest.main()