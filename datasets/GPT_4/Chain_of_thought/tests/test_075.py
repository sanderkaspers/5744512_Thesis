import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_075 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_negativenum([1, -2, 3, -4, 5]), -6)

    def test_all_positive_numbers(self):
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5]), -15)

    def test_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_list_with_zero(self):
        self.assertEqual(sum_negativenum([0, -1, 2, -3]), -4)

    def test_mixed_data_types(self):
        self.assertEqual(sum_negativenum([1.5, -2.5, 3.5, -4.5]), -7.0)

    def test_large_numbers(self):
        self.assertEqual(sum_negativenum([1e10, -1e10, 1e5, -1e5]), -10000100000.0)

    def test_repeated_negative_numbers(self):
        self.assertEqual(sum_negativenum([-1, -1, -1, -1]), -4)

    def test_no_negative_numbers(self):
        self.assertEqual(sum_negativenum([1, 2, 3, 4]), 0)

    def test_only_zero(self):
        self.assertEqual(sum_negativenum([0]), 0)

