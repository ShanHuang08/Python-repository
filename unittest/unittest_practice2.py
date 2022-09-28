import unittest

def compare_string(s1, s2):
    if s1 == s2:
        return True
    else:
        return False

class MyFirstTest(unittest.TestCase):

    def setUp(self):
        self.default_greeting = "Hello"

    def test_compare_stringT(self):
        test_greeting = "Hello"
        # self.assertFalse(compare_string(self.default_greeting, test_greeting))
        self.assertTrue(compare_string(self.default_greeting, test_greeting))

    def test_compare_stringF(self):
        test_greeting = "HellO" #大寫O
        self.assertFalse(compare_string(self.default_greeting, test_greeting))
        # self.assertTrue(compare_string(self.default_greeting, test_greeting))

    def test_compare_hex_string(self):
        hex_greeting = b"\x48\x65\x6c\x6c\x6f"
        # self.assertTrue(compare_string(self.default_greeting, hex_greeting))
        self.assertFalse(compare_string(self.default_greeting, hex_greeting))


if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromTestCase(MyFirstTest)
    unittest.TextTestRunner(verbosity=2).run(tests)