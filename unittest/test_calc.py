import unittest
import calc

class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        # print('setup')
        pass

    def tearDown(self) -> None:
        # print('teardowm\n')
        pass

    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        # print('add')

    def test_substract(self):
        self.assertEqual(calc.substract(10,5),5)
        # print('substract')

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertRaises(ValueError,calc.multiply,10,0)
        with self.assertRaises(ValueError):
            self.assertRaises(calc.multiply(10,0),0)
        # print('multiply')    

    def test_division(self):
        self.assertEqual(calc.division(10,5),2)
        self.assertRaises(ValueError,calc.division,10,0)
        with self.assertRaises(ValueError):
            self.assertRaises(calc.division(10,0),0)
        # print('division')

if __name__=='__main__':
    unittest.main()