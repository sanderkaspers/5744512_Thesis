import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_075 import *

class TestVersion(unittest.TestCase):
    def test_mixed_values(self): self.assertEqual(sum_negativenum([1, -2, 3, -4, 5]), -6)

    def test_all_positive(self): self.assertEqual(sum_negativenum([1, 2, 3]), 0)

    def test_all_negative(self): self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_empty_list(self): self.assertEqual(sum_negativenum([]), 0)

    def test_single_negative(self): self.assertEqual(sum_negativenum([-7]), -7)

    def test_with_zero(self): self.assertEqual(sum_negativenum([-2, 0, 1]), -2)

    def test_large_list(self): self.assertEqual(sum_negativenum([-1]*1000 + [2]*1000), -1000)

    def test_with_floats(self): self.assertEqual(sum_negativenum([-1.5, -2.5, 0]), -4.0)

