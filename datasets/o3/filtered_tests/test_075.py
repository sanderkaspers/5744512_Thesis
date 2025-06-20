import unittest
from datasets.o3.programs.program_075 import *

class TestVersion(unittest.TestCase):
    def test_mixed_numbers_returns_sum_negatives(self):
        nums = [1,-2,3,-4]
        self.assertEqual(sum_negativenum(nums), -6)

    def test_all_positive_returns_zero(self):
        nums = [1,2,3]
        self.assertEqual(sum_negativenum(nums), 0)

    def test_empty_list_returns_zero(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_all_negative_numbers(self):
        nums = [-1,-2,-3]
        self.assertEqual(sum_negativenum(nums), -6)

    def test_float_numbers_negative_sum(self):
        nums = [-1.5,2.0,-3.5]
        self.assertAlmostEqual(sum_negativenum(nums), -5.0)

