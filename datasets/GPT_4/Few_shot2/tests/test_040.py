import unittest
from datasets.GPT_4.Few_shot2.programs.program_040 import *

class TestVersion(unittest.TestCase):
    def test_is_undulating_valid_odd_length(self): self.assertTrue(is_undulating(121))

    def test_is_undulating_valid_even_length(self): self.assertTrue(is_undulating(2323))

    def test_is_undulating_too_short(self): self.assertFalse(is_undulating(12))

    def test_is_undulating_same_starting_digits(self): self.assertFalse(is_undulating(112))

    def test_is_undulating_break_pattern(self): self.assertFalse(is_undulating(12321))

    def test_is_undulating_alternating_digits(self): self.assertTrue(is_undulating(434343))

    def test_is_undulating_three_digits_same(self): self.assertFalse(is_undulating(111))

    def test_is_undulating_valid_long(self): self.assertTrue(is_undulating(78787878))

    def test_is_undulating_start_with_zero(self): self.assertTrue(is_undulating(int('10101')))

