import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_009 import *

class TestVersion(unittest.TestCase):
    def test_typical_number(self): self.assertEqual(rev(12345), 54321)

    def test_trailing_zeros(self): self.assertEqual(rev(1200), 21)

    def test_single_digit(self): self.assertEqual(rev(7), 7)

    def test_zero(self): self.assertEqual(rev(0), 0)

    def test_large_number(self): self.assertEqual(rev(9876543210), 123456789)

    def test_negative_number(self): self.assertEqual(rev(-123), 0)

    def test_palindrome_number(self): self.assertEqual(rev(1221), 1221)

