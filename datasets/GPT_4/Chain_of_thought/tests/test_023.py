import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_023 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(comb_sort([4, 3, 2, 5, 1]), [1, 2, 3, 4, 5])

    def test_already_sorted(self):
        self.assertEqual(comb_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(comb_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_single_element(self):
        self.assertEqual(comb_sort([1]), [1])

    def test_empty_list(self):
        self.assertEqual(comb_sort([]), [])

    def test_all_identical_elements(self):
        self.assertEqual(comb_sort([7, 7, 7, 7]), [7, 7, 7, 7])

    def test_large_numbers(self):
        self.assertEqual(comb_sort([100000, 99999, 99998]), [99998, 99999, 100000])

    def test_negative_numbers(self):
        self.assertEqual(comb_sort([-5, -1, -3, -2, -4]), [-5, -4, -3, -2, -1])

    def test_mixed_positive_negative(self):
        self.assertEqual(comb_sort([3, -2, -1, 4, 0]), [-2, -1, 0, 3, 4])

    def test_floating_point_numbers(self):
        self.assertEqual(comb_sort([1.5, 3.2, 2.1, 4.8, 0.5]), [0.5, 1.5, 2.1, 3.2, 4.8])

    def test_large_list(self):
        large_list = list(range(1000, 0, -1))
        sorted_list = list(range(1, 1001))
        self.assertEqual(comb_sort(large_list), sorted_list)

    def test_boundary_values(self):
        self.assertEqual(comb_sort([2147483647, -2147483648, 0]), [-2147483648, 0, 2147483647])

