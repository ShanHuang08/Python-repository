<<<<<<< HEAD
import unittest
import calc

class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        # print('setup')
        pass

    def tearDown(self) -> None:
        # print('teardown\n')
        pass

    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        if calc.add(10,5)==15:
            testValue=True
            message=''
        else:
            testValue=False
            message='Test value is not true'
        self.assertTrue(testValue,message)
        # print('add')

    def test_substract(self):
        self.assertEqual(calc.substract(10,5),5)
        if calc.substract(10,5)==5:
            testValue=True
        else:
            testValue=False
        self.assertTrue(testValue,'Test value is not true')
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
=======
import unittest
import calc

class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        # print('setup')
        pass

    def tearDown(self) -> None:
        # print('teardown\n')
        pass

    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        if calc.add(10,5)==15:
            testValue=True
            message=''
        else:
            testValue=False
            message='Test value is not true'
        self.assertTrue(testValue,message)
        # print('add')

    def test_substract(self):
        self.assertEqual(calc.substract(10,5),5)
        if calc.substract(10,5)==5:
            testValue=True
        else:
            testValue=False
        self.assertTrue(testValue,'Test value is not true')
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
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
    unittest.main()