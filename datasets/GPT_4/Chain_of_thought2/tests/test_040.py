import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_040 import *

class TestVersion(unittest.TestCase):
    def test_simple_undulating(self): self.assertTrue(is_undulating(121))

    def test_long_undulating(self): self.assertTrue(is_undulating(232323))

    def test_valid_even_length(self): self.assertTrue(is_undulating(1212))

    def test_non_undulating_pattern(self): self.assertFalse(is_undulating(1234))

    def test_breaks_pattern_late(self): self.assertFalse(is_undulating(1213))

    def test_single_digit(self): self.assertFalse(is_undulating(7))

    def test_two_digits(self): self.assertFalse(is_undulating(12))

    def test_same_digit_repeated(self): self.assertFalse(is_undulating(1111))

    def test_three_same_digits(self): self.assertFalse(is_undulating(333))

    def test_input_as_string_number(self): self.assertTrue(is_undulating('343434'))

