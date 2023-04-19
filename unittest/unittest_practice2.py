<<<<<<< HEAD
import unittest

def compare_string(s1, s2):
    if s1 == s2:
        return True
    else:
        return False

class MyFirstTest(unittest.TestCase):

    def setUp(self):
        self.default_str = "Hello"

    def test_compare_stringT(self):
        test_str = "Hello"
        message=test_str+" isn't incorrect"
        # self.assertFalse(compare_string(self.default_greeting, test_greeting))
        self.assertTrue(compare_string(self.default_str, test_str),message)

    def test_compare_stringF(self):
        test_str = "HellO" #大寫O
        message='Error msg'
        self.assertFalse(compare_string(self.default_str, test_str),message)
        # self.assertTrue(compare_string(self.default_greeting, test_greeting))

    def test_compare_hex_string(self):
        test_str = b"\x48\x65\x6c\x6c\x6f"
        message='Error msg'
        # self.assertTrue(compare_string(self.default_greeting, hex_greeting))
        self.assertFalse(compare_string(self.default_str, test_str),message)


if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromTestCase(MyFirstTest)
    unittest.TextTestRunner(verbosity=2).run(tests)
=======
import unittest

def compare_string(s1, s2):
    if s1 == s2:
        return True
    else:
        return False

class MyFirstTest(unittest.TestCase):

    def setUp(self):
        self.default_str = "Hello"

    def test_compare_stringT(self):
        test_str = "Hello"
        message=test_str+" isn't incorrect"
        # self.assertFalse(compare_string(self.default_greeting, test_greeting))
        self.assertTrue(compare_string(self.default_str, test_str),message)

    def test_compare_stringF(self):
        test_str = "HellO" #大寫O
        message='Error msg'
        self.assertFalse(compare_string(self.default_str, test_str),message)
        # self.assertTrue(compare_string(self.default_greeting, test_greeting))

    def test_compare_hex_string(self):
        test_str = b"\x48\x65\x6c\x6c\x6f"
        message='Error msg'
        # self.assertTrue(compare_string(self.default_greeting, hex_greeting))
        self.assertFalse(compare_string(self.default_str, test_str),message)


if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromTestCase(MyFirstTest)
    unittest.TextTestRunner(verbosity=2).run(tests)
>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
