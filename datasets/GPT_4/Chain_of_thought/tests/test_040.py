import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_040 import *

class TestVersion(unittest.TestCase):
    def test_typical_undulating(self):
        self.assertTrue(is_undulating(121212))

    def test_non_undulating(self):
        self.assertFalse(is_undulating(12345))

    def test_short_number(self):
        self.assertFalse(is_undulating(12))

    def test_single_digit(self):
        self.assertFalse(is_undulating(7))

    def test_two_digit_number(self):
        self.assertFalse(is_undulating(88))

    def test_negative_number(self):
        self.assertFalse(is_undulating(-121212))

    def test_large_undulating_number(self):
        self.assertTrue(is_undulating(12121212121212121212))

    def test_all_same_digits(self):
        self.assertFalse(is_undulating(11111))

    def test_alternating_start_different(self):
        self.assertTrue(is_undulating(2121))

