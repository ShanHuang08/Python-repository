<<<<<<< HEAD
from typing import ValuesView
import unittest
from BintoHex import DigitBintoHex
from DecConvert import *

class BinTestCases(unittest.TestCase):
    def test_BintoHex(self):
        self.assertEqual(DigitBintoHex('1000'),'8')
        self.assertEqual(DigitBintoHex(1000),'8')
        self.assertEqual(DigitBintoHex('1011110011111111011110111111010111111111'),'bcff7bf5ff')
        self.assertEqual(DigitBintoHex(1011110011111111011110111111010111111111),'bcff7bf5ff')
        self.assertEqual(DigitBintoHex(True),1)
    
    def test_DectoBin(self):
        self.assertEqual(BinConvert(100),'1100100')
        self.assertEqual(BinConvert('100'),'1100100') 
        self.assertEqual(BinConvert(15),'1111')
        self.assertEqual(BinConvert('15'),'1111')

    def test_BintoDec(self):
        self.assertEqual(BintoDec('1111'),15)
        self.assertEqual(BintoDec(1111),15)

    def test_error(self):
        with self.assertRaises(TypeError):
            BintoDec(True)
        with self.assertRaises(ValueError):
            BintoDec(12)
        with self.assertRaises(TypeError):
            DigitBintoHex('a')
            DigitBintoHex(123)
            DigitBintoHex('123')


if __name__ == '__main__':
    unittest.main()
=======
from typing import ValuesView
import unittest
from BintoHex import DigitBintoHex
from DecConvert import *

class BinTestCases(unittest.TestCase):
    def test_BintoHex(self):
        self.assertEqual(DigitBintoHex('1000'),'8')
        self.assertEqual(DigitBintoHex(1000),'8')
        self.assertEqual(DigitBintoHex('1011110011111111011110111111010111111111'),'bcff7bf5ff')
        self.assertEqual(DigitBintoHex(1011110011111111011110111111010111111111),'bcff7bf5ff')
        self.assertEqual(DigitBintoHex(True),1)
    
    def test_DectoBin(self):
        self.assertEqual(BinConvert(100),'1100100')
        self.assertEqual(BinConvert('100'),'1100100') 
        self.assertEqual(BinConvert(15),'1111')
        self.assertEqual(BinConvert('15'),'1111')

    def test_BintoDec(self):
        self.assertEqual(BintoDec('1111'),15)
        self.assertEqual(BintoDec(1111),15)

    def test_error(self):
        with self.assertRaises(TypeError):
            BintoDec(True)
        with self.assertRaises(ValueError):
            BintoDec(12)
        with self.assertRaises(TypeError):
            DigitBintoHex('a')
            DigitBintoHex(123)
            DigitBintoHex('123')


if __name__ == '__main__':
    unittest.main()
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
    