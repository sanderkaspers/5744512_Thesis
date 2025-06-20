import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_014 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(smallest_num([3, 1, 4, 2]), 1)

    def test_single_element(self):
        self.assertEqual(smallest_num([5]), 5)

    def test_all_identical_elements(self):
        self.assertEqual(smallest_num([7, 7, 7, 7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(smallest_num([-1, -5, -3]), -5)

    def test_mixed_positive_negative(self):
        self.assertEqual(smallest_num([3, -2, 4, 0]), -2)

    def test_list_with_zero(self):
        self.assertEqual(smallest_num([0, 5, 3]), 0)

    def test_large_numbers(self):
        self.assertEqual(smallest_num([10**6, 10**12, 10**8]), 10**6)

    def test_small_numbers(self):
        self.assertEqual(smallest_num([0.0001, 0.0002, 0.0003]), 0.0001)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            smallest_num([])

    def test_floating_point_numbers(self):
        self.assertEqual(smallest_num([2.5, 3.1, 0.1]), 0.1)

    def test_repeated_smallest_number(self):
        self.assertEqual(smallest_num([5, 2, 2, 3]), 2)

    def test_max_min_integers(self):
        self.assertEqual(smallest_num([2147483647, -2147483648]), -2147483648)

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            smallest_num([3, 'a', 2])

