import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_072 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)

    def test_all_elements_unique(self):
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), 1)

    def test_all_elements_same(self):
        self.assertEqual(max_occurrences([2, 2, 2, 2]), 2)

    def test_multiple_max_frequencies(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3]), 1)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max_occurrences([])

    def test_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -1, -2, -2, -3]), -1)

    def test_mixed_data_types(self):
        self.assertEqual(max_occurrences([1, '1', 2, '2', '1']), '1')

    def test_very_large_list(self):
        large_list = [1] * 1000000 + [2] * 999999
        self.assertEqual(max_occurrences(large_list), 1)

    def test_floating_point_numbers(self):
        self.assertEqual(max_occurrences([1.1, 2.2, 3.3, 1.1, 1.1]), 1.1)

    def test_special_characters(self):
        self.assertEqual(max_occurrences(['@', '@', '#', '#', '@']), '@')

