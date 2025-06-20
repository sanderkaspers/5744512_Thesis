import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_058 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_integer('12345'))

    def test_negative_integer(self):
        self.assertTrue(check_integer('-12345'))

    def test_leading_trailing_whitespace(self):
        self.assertTrue(check_integer('  12345  '))
        self.assertTrue(check_integer('  -12345  '))

    def test_non_digit_characters(self):
        self.assertFalse(check_integer('123a45'))
        self.assertFalse(check_integer('12@45'))

    def test_empty_string(self):
        self.assertIsNone(check_integer(''))

    def test_only_sign(self):
        self.assertFalse(check_integer('+'))
        self.assertFalse(check_integer('-'))

    def test_mixed_digits_and_letters(self):
        self.assertFalse(check_integer('12a34'))

    def test_decimal_point(self):
        self.assertFalse(check_integer('123.45'))

    def test_multiple_signs(self):
        self.assertFalse(check_integer('++12345'))
        self.assertFalse(check_integer('--12345'))

    def test_large_integer(self):
        self.assertTrue(check_integer('12345678901234567890'))

