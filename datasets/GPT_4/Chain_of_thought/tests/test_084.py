import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_084 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_Abs_Diff([1, -2, 5, 10, -8]), 18)

    def test_all_positive_numbers(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5]), 4)

    def test_all_negative_numbers(self):
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4, -5]), 4)

    def test_single_element_array(self):
        self.assertEqual(max_Abs_Diff([10]), 0)

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            max_Abs_Diff([])

    def test_repeated_elements(self):
        self.assertEqual(max_Abs_Diff([7, 7, 7, 7]), 0)

    def test_array_with_zero(self):
        self.assertEqual(max_Abs_Diff([0, -2, 5, 10]), 12)

    def test_large_numbers(self):
        self.assertEqual(max_Abs_Diff([1000000, -1000000, 999999, -999999]), 2000000)

    def test_floating_point_numbers(self):
        self.assertEqual(max_Abs_Diff([1.5, -2.5, 3.5, -4.5]), 8.0)

    def test_consecutive_numbers(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5]), 4)

