import unittest
from datasets.GPT_4.Few_shot.programs.program_058 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(check_integer("123"), True) # Positive integer)

    def test_case_2(self):
        self.assertEqual(check_integer("-123"), False) # Negative integer (function does not handle this))

    def test_case_3(self):
        self.assertEqual(check_integer("abc"), False) # Non-digit characters)

    def test_case_4(self):
        self.assertEqual(check_integer(""), False) # Empty string)

    def test_case_5(self):
        self.assertEqual(check_integer("  456  "), True) # Integer with spaces)

    def test_case_6(self):
        self.assertEqual(check_integer("007"), True) # Integer with leading zeros)

    def test_case_7(self):
        self.assertEqual(check_integer("12a3"), False) # Alphanumeric)

    def test_case_8(self):
        self.assertEqual(check_integer("+123"), False) # Positive sign)

