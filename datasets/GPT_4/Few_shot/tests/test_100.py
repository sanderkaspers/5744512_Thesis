import unittest
from datasets.GPT_4.Few_shot.programs.program_100 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(odd_values_string("abcdef"), "bdf") # Even number of characters)

    def test_case_2(self):
        self.assertEqual(odd_values_string("abcde"), "bd") # Odd number of characters)

    def test_case_3(self):
        self.assertEqual(odd_values_string("a"), "") # Single character string)

    def test_case_4(self):
        self.assertEqual(odd_values_string(""), "") # Empty string)

    def test_case_5(self):
        self.assertEqual(odd_values_string("abcdefg"), "bdf") # Odd-length string)

    def test_case_6(self):
        self.assertEqual(odd_values_string("0123456789"), "13579") # Numeric characters)

    def test_case_7(self):
        self.assertEqual(odd_values_string("!@) #$%^"), "@$^")  # Special characters)

    def test_case_8(self):
        self.assertEqual(odd_values_string("Python"), "yhn") # Mixed-case string)

