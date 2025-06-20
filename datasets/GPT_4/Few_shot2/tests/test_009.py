import unittest
from datasets.GPT_4.Few_shot2.programs.program_009 import *

class TestVersion(unittest.TestCase):
    def test_rev_single_digit(self): self.assertEqual(rev(5), 5)

    def test_rev_two_digits(self): self.assertEqual(rev(42), 24)

    def test_rev_multiple_digits(self): self.assertEqual(rev(123456), 654321)

    def test_rev_number_with_trailing_zeros(self): self.assertEqual(rev(1200), 21)

    def test_rev_zero(self): self.assertEqual(rev(0), 0)

    def test_rev_palindromic_number(self): self.assertEqual(rev(1221), 1221)

    def test_rev_negative(self): self.assertEqual(rev(-123), -321)

    def test_rev_large_number(self): self.assertEqual(rev(9876543210), 123456789)

