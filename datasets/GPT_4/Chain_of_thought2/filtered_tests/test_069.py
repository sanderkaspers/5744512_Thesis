import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_069 import *

class TestVersion(unittest.TestCase):
    def test_two_positives(self): self.assertEqual(multiply_int(3, 4), 12)

    def test_x_zero(self): self.assertEqual(multiply_int(0, 5), 0)

    def test_y_zero(self): self.assertEqual(multiply_int(7, 0), 0)

    def test_multiply_with_one(self): self.assertEqual(multiply_int(9, 1), 9)

    def test_multiply_with_negative_y(self): self.assertEqual(multiply_int(4, -3), -12)

    def test_multiply_with_negative_x(self): self.assertEqual(multiply_int(-5, 2), -10)

    def test_both_negative(self): self.assertEqual(multiply_int(-6, -4), 24)

    def test_both_zero(self): self.assertEqual(multiply_int(0, 0), 0)

    def test_negative_one_operand(self): self.assertEqual(multiply_int(-1, 5), -5); self.assertEqual(multiply_int(5, -1), -5)

    def test_large_values(self): self.assertEqual(multiply_int(2, 100), 200)

