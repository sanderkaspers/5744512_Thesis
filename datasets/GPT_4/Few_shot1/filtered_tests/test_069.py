import unittest
from datasets.GPT_4.Few_shot1.programs.program_069 import *

class TestVersion(unittest.TestCase):
    def test_multiply_int_positive(self): self.assertEqual(multiply_int(3, 4), 12)

    def test_multiply_int_zero_y(self): self.assertEqual(multiply_int(5, 0), 0)

    def test_multiply_int_zero_x(self): self.assertEqual(multiply_int(0, 5), 0)

    def test_multiply_int_y_is_one(self): self.assertEqual(multiply_int(7, 1), 7)

    def test_multiply_int_negative_y(self): self.assertEqual(multiply_int(6, -2), -12)

    def test_multiply_int_negative_x(self): self.assertEqual(multiply_int(-3, 4), -12)

    def test_multiply_int_both_negatives(self): self.assertEqual(multiply_int(-2, -3), 6)

    def test_multiply_int_large_values(self): self.assertEqual(multiply_int(100, 3), 300)

    def test_multiply_int_negative_y_one(self): self.assertEqual(multiply_int(9, -1), -9)

    def test_multiply_int_negative_x_one(self): self.assertEqual(multiply_int(-1, 9), -9)

