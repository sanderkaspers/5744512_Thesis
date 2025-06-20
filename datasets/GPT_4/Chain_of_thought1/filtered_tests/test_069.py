import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_069 import *

class TestVersion(unittest.TestCase):
    def test_positive_positive(self): self.assertEqual(multiply_int(3, 4), 12)

    def test_positive_zero(self): self.assertEqual(multiply_int(5, 0), 0)

    def test_zero_positive(self): self.assertEqual(multiply_int(0, 5), 0)

    def test_positive_negative(self): self.assertEqual(multiply_int(4, -3), -12)

    def test_negative_positive(self): self.assertEqual(multiply_int(-3, 4), -12)

    def test_negative_negative(self): self.assertEqual(multiply_int(-2, -3), 6)

    def test_zero_zero(self): self.assertEqual(multiply_int(0, 0), 0)

    def test_large_small(self): self.assertEqual(multiply_int(1000, 1), 1000)

    def test_large_zero(self): self.assertEqual(multiply_int(9999, 0), 0)

