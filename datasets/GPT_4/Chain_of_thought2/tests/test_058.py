import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_058 import *

class TestVersion(unittest.TestCase):
    def test_valid_integer(self): self.assertTrue(check_integer('123'))

    def test_valid_signed_integer_positive(self): self.assertTrue(check_integer('+456'))

    def test_valid_signed_integer_negative(self): self.assertTrue(check_integer('-789'))

    def test_valid_integer_with_whitespace(self): self.assertTrue(check_integer('   42  '))

    def test_empty_string(self): self.assertIsNone(check_integer(''))

    def test_whitespace_only(self): self.assertIsNone(check_integer('   '))

    def test_non_numeric_characters(self): self.assertFalse(check_integer('12a'))

    def test_multiple_signs(self): self.assertFalse(check_integer('--5'))

    def test_only_sign(self): self.assertFalse(check_integer('+')); self.assertFalse(check_integer('-'))

    def test_embedded_whitespace(self): self.assertFalse(check_integer('1 2 3'))

    def test_float_string(self): self.assertFalse(check_integer('12.3'))

    def test_scientific_notation_string(self): self.assertFalse(check_integer('1e3'))

    def test_unicode_digits(self): self.assertFalse(check_integer('１２３'))

    def test_leading_trailing_tabs_and_newlines(self): self.assertTrue(check_integer('\n\t 321 \t\n'))

