import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_040 import *

class TestVersion(unittest.TestCase):
    def test_121(self): self.assertTrue(is_undulating(121))

    def test_343434(self): self.assertTrue(is_undulating(343434))

    def test_7878(self): self.assertTrue(is_undulating(7878))

    def test_898989(self): self.assertTrue(is_undulating(898989))

    def test_single_digit(self): self.assertFalse(is_undulating(1))

    def test_two_digits(self): self.assertFalse(is_undulating(12))

    def test_123(self): self.assertFalse(is_undulating(123))

    def test_all_same(self): self.assertFalse(is_undulating(111))

    def test_palindrome(self): self.assertFalse(is_undulating(1221))

    def test_partial_pattern(self): self.assertFalse(is_undulating(1314))

    def test_string_input(self): self.assertTrue(is_undulating('1212'))

    def test_float_input(self): self.assertFalse(is_undulating(12.12))

