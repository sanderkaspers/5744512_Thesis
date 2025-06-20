import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_081 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(pancake_sort([3, 6, 1, 8, 4]), [1, 3, 4, 6, 8])

    def test_already_sorted_list(self):
        self.assertEqual(pancake_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(pancake_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_single_element_list(self):
        self.assertEqual(pancake_sort([1]), [1])

    def test_empty_list(self):
        self.assertEqual(pancake_sort([]), [])

    def test_list_with_duplicates(self):
        self.assertEqual(pancake_sort([4, 5, 5, 3, 4]), [3, 4, 4, 5, 5])

    def test_list_with_negative_numbers(self):
        self.assertEqual(pancake_sort([-1, -3, -2, 0, 2]), [-3, -2, -1, 0, 2])

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            pancake_sort([1, '2', 3])

    def test_large_list(self):
        large_list = list(range(1000, 0, -1))
        self.assertEqual(pancake_sort(large_list), list(range(1, 1001)))

    def test_floating_point_numbers(self):
        self.assertEqual(pancake_sort([1.1, 2.2, 0.5, 3.3]), [0.5, 1.1, 2.2, 3.3])

