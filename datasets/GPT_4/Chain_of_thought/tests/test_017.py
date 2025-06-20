import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_017 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(recursive_list_sum([1, [2, 3], 4, [5, [6]]]), 21)

    def test_single_element_list(self):
        self.assertEqual(recursive_list_sum([10]), 10)

    def test_deeply_nested_list(self):
        self.assertEqual(recursive_list_sum([1, [2, [3, [4, [5]]]]]), 15)

    def test_all_elements_as_lists(self):
        self.assertEqual(recursive_list_sum([[1, 2], [3, 4], [5, 6]]), 21)

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_empty_nested_lists(self):
        self.assertEqual(recursive_list_sum([[], [[], []]]), 0)

    def test_negative_numbers(self):
        self.assertEqual(recursive_list_sum([1, [-2, 3], [-4, [5, [-6]]]]), -3)

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            recursive_list_sum([1, 'two', 3.0])

    def test_floating_point_numbers(self):
        self.assertEqual(recursive_list_sum([1.5, [2.5, 3.0], 4.0]), 11.0)

    def test_large_numbers(self):
        self.assertEqual(recursive_list_sum([1000000, [2000000, 3000000]]), 6000000)

    def test_mixed_positive_negative(self):
        self.assertEqual(recursive_list_sum([1, [-2, 3], -4]), -2)

    def test_zero_element(self):
        self.assertEqual(recursive_list_sum([0, [0, 0], 0]), 0)

    def test_all_zero_elements(self):
        self.assertEqual(recursive_list_sum([0, [0, 0], [0]]), 0)

    def test_single_nested_list(self):
        self.assertEqual(recursive_list_sum([[1, 2, 3]]), 6)

