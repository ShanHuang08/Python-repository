import unittest
from unittest.case import _AssertRaisesContext
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2,3),5)
        self.assertEqual(calc.add(5,5),10)
    
    def test_substract(self):
        self.assertEqual(calc.substract(2,3),-1)
        self.assertEqual(calc.substract(3,2),1)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(3,4),12)
        self.assertEqual(calc.multiply(3,2),6)

    def test_division(self):
        self.assertEqual(calc.division(10,2),5)
        self.assertEqual(calc.division(10,0),0)
        with self.assertRaises(ValueError):
            calc.division(10,0)

if __name__=='__main__':
    unittest.main()