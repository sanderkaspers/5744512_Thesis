import unittest
from datasets.GPT_4.Few_shot2.programs.program_069 import *

class TestVersion(unittest.TestCase):
    def test_multiply_int_positive(self): self.assertEqual(multiply_int(3, 4), 12)

    def test_multiply_int_zero(self): self.assertEqual(multiply_int(5, 0), 0)

    def test_multiply_int_zero_reverse(self): self.assertEqual(multiply_int(0, 7), 0)

    def test_multiply_int_negative_y(self): self.assertEqual(multiply_int(4, -3), -12)

    def test_multiply_int_negative_x(self): self.assertEqual(multiply_int(-4, 3), -12)

    def test_multiply_int_both_negative(self): self.assertEqual(multiply_int(-4, -2), 8)

    def test_multiply_int_one(self): self.assertEqual(multiply_int(1, 5), 5)

    def test_multiply_int_negative_one(self): self.assertEqual(multiply_int(-1, 6), -6)

    def test_multiply_int_large(self): self.assertEqual(multiply_int(10, 10), 100)

