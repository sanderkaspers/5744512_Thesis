import unittest
from datasets.GPT_4.Few_shot1.programs.program_075 import *

class TestVersion(unittest.TestCase):
    def test_sum_negativenum_basic(self): self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_sum_negativenum_mixed(self): self.assertEqual(sum_negativenum([1, -2, 3, -4]), -6)

    def test_sum_negativenum_all_positive(self): self.assertEqual(sum_negativenum([1, 2, 3]), 0)

    def test_sum_negativenum_all_zero(self): self.assertEqual(sum_negativenum([0, 0, 0]), 0)

    def test_sum_negativenum_empty_list(self): self.assertEqual(sum_negativenum([]), 0)

    def test_sum_negativenum_single_negative(self): self.assertEqual(sum_negativenum([-5]), -5)

    def test_sum_negativenum_single_positive(self): self.assertEqual(sum_negativenum([5]), 0)

    def test_sum_negativenum_with_zero(self): self.assertEqual(sum_negativenum([-1, 0, 1]), -1)

    def test_sum_negativenum_large_values(self): self.assertEqual(sum_negativenum([-1000, -2000]), -3000)

    def test_sum_negativenum_floats(self): self.assertEqual(sum_negativenum([-1.5, -2.5, 3.0]), -4.0)

