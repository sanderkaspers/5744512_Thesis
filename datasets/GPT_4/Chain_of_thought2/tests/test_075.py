import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_075 import *

class TestVersion(unittest.TestCase):
    def test_all_negatives(self): self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_all_positives(self): self.assertEqual(sum_negativenum([1, 2, 3]), 0)

    def test_mixed_numbers(self): self.assertEqual(sum_negativenum([-5, 10, -15, 20]), -20)

    def test_with_zero(self): self.assertEqual(sum_negativenum([-2, 0, 3]), -2)

    def test_empty_list(self): self.assertEqual(sum_negativenum([]), 0)

    def test_single_negative(self): self.assertEqual(sum_negativenum([-42]), -42)

    def test_single_positive(self): self.assertEqual(sum_negativenum([7]), 0)

    def test_large_negative_numbers(self): self.assertEqual(sum_negativenum([-1000, -999]), -1999)

    def test_floats_and_integers(self): self.assertEqual(sum_negativenum([-1.5, 2, -3.5]), -5.0)

