import unittest
from datasets.GPT_4.Few_shot2.programs.program_058 import *

class TestVersion(unittest.TestCase):
    def test_check_integer_basic_digit(self): self.assertTrue(check_integer('123'))

    def test_check_integer_with_leading_spaces(self): self.assertTrue(check_integer('   456'))

    def test_check_integer_with_trailing_spaces(self): self.assertTrue(check_integer('789   '))

    def test_check_integer_with_leading_and_trailing_spaces(self): self.assertTrue(check_integer('  101  '))

    def test_check_integer_with_internal_space(self): self.assertFalse(check_integer('12 34'))

    def test_check_integer_with_letters(self): self.assertFalse(check_integer('abc'))

    def test_check_integer_with_alphanumeric(self): self.assertFalse(check_integer('123abc'))

    def test_check_integer_empty_string(self): self.assertFalse(check_integer(''))

    def test_check_integer_only_spaces(self): self.assertFalse(check_integer('   '))

    def test_check_integer_negative_number(self): self.assertFalse(check_integer('-123'))

    def test_check_integer_float_number(self): self.assertFalse(check_integer('12.34'))

