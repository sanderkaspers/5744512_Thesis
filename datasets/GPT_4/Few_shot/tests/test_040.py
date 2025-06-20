import unittest
from datasets.GPT_4.Few_shot.programs.program_040 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_undulating(121212), True) # Classic undulating number)

    def test_case_2(self):
        self.assertEqual(is_undulating(123123), False) # More than two unique digits)

    def test_case_3(self):
        self.assertEqual(is_undulating(11), False) # Repeating digits, not undulating)

    def test_case_4(self):
        self.assertEqual(is_undulating(12), True) # Simple undulating number)

    def test_case_5(self):
        self.assertEqual(is_undulating(9), False) # Single-digit number)

    def test_case_6(self):
        self.assertEqual(is_undulating(121), True) # Three-digit undulating number)

    def test_case_7(self):
        self.assertEqual(is_undulating(12321), False) # Palindrome but not undulating)

    def test_case_8(self):
        self.assertEqual(is_undulating(10101010), True) # Long undulating number)

