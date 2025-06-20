import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_058 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer(self): self.assertTrue(check_integer('123'))

    def test_negative_integer(self): self.assertTrue(check_integer('-123'))

    def test_plus_sign_integer(self): self.assertTrue(check_integer('+456'))

    def test_whitespace_integer(self): self.assertTrue(check_integer('   789   '))

    def test_sign_only(self): self.assertFalse(check_integer('+')); self.assertFalse(check_integer('-'))

    def test_empty_string(self): self.assertFalse(check_integer(''))

    def test_zero(self): self.assertTrue(check_integer('0'))

    def test_alphanumeric(self): self.assertFalse(check_integer('12a')); self.assertFalse(check_integer('abc'))

    def test_decimal(self): self.assertFalse(check_integer('3.14'))

    def test_leading_zeros(self): self.assertTrue(check_integer('007'))

    def test_whitespace_only(self): self.assertFalse(check_integer('    '))

    def test_sign_with_space(self): self.assertFalse(check_integer('+ 5'))

    def test_sign_not_at_start(self): self.assertFalse(check_integer('5-'))

    def test_negative_float_string(self): self.assertFalse(check_integer('-3.0'))

    def test_unicode_digits(self): self.assertTrue(check_integer('１２３'))

