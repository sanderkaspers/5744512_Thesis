import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_009 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check(12))

    def test_no_match_case(self):
        self.assertFalse(check(23))

    def test_single_digit(self):
        self.assertFalse(check(5))

    def test_trailing_zeros(self):
        self.assertFalse(check(100))

    def test_palindrome(self):
        self.assertFalse(check(121))

    def test_negative_number(self):
        self.assertFalse(check(-12))

    def test_large_number(self):
        self.assertFalse(check(123456789))

    def test_zero_input(self):
        self.assertFalse(check(0))

    def test_even_digits(self):
        self.assertFalse(check(42))

    def test_odd_digits(self):
        self.assertFalse(check(543))

    def test_boundary_condition(self):
        self.assertFalse(check(21))

    def test_floating_point_number(self):
        with self.assertRaises(TypeError):
            check(12.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            check('12')

    def test_close_to_match(self):
        self.assertFalse(check(11))

