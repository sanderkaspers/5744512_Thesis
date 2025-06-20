import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_093 import *

class TestVersion(unittest.TestCase):
    def test_multiple_occurrences(self):
        self.assertEqual(frequency([1, 2, 3, 1, 4, 1], 1), 3)

    def test_no_occurrences(self):
        self.assertEqual(frequency([1, 2, 3, 4], 5), 0)

    def test_single_occurrence(self):
        self.assertEqual(frequency([1, 2, 3, 4], 3), 1)

    def test_empty_list(self):
        self.assertEqual(frequency([], 1), 0)

    def test_all_elements_are_x(self):
        self.assertEqual(frequency([7, 7, 7, 7], 7), 4)

    def test_different_data_types(self):
        self.assertEqual(frequency([1, '1', 1.0], 1), 2)

    def test_large_list(self):
        large_list = [5] * 10000 + [10]
        self.assertEqual(frequency(large_list, 5), 10000)

    def test_negative_numbers(self):
        self.assertEqual(frequency([-1, -2, -3, -1], -1), 2)

    def test_floating_point_x(self):
        self.assertEqual(frequency([1.5, 2.5, 1.5], 1.5), 2)

    def test_duplicates_of_non_x(self):
        self.assertEqual(frequency([1, 2, 2, 3, 4, 4], 5), 0)

