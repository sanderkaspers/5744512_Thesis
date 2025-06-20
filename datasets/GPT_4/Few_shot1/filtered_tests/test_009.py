import unittest
from datasets.GPT_4.Few_shot1.programs.program_009 import *

class TestVersion(unittest.TestCase):
    def test_rev_single_digit(self): self.assertEqual(rev(7), 7)

    def test_rev_two_digits(self): self.assertEqual(rev(12), 21)

    def test_rev_multiple_digits(self): self.assertEqual(rev(1234), 4321)

    def test_rev_with_zero_end(self): self.assertEqual(rev(1200), 21)

    def test_rev_zero(self): self.assertEqual(rev(0), 0)

    def test_rev_large_number(self): self.assertEqual(rev(9876543210), 123456789)

