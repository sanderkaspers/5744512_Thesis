import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_045 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(frequency_lists([[1, 2, 3], [1, 2], [3, 4]]), {1: 2, 2: 2, 3: 2, 4: 1})

    def test_empty_list_of_lists(self):
        self.assertEqual(frequency_lists([[], []]), {})

    def test_single_element_lists(self):
        self.assertEqual(frequency_lists([[1], [2], [3]]), {1: 1, 2: 1, 3: 1})

    def test_duplicate_elements(self):
        self.assertEqual(frequency_lists([[1, 2, 2], [2, 3, 3], [3, 4]]), {1: 1, 2: 3, 3: 3, 4: 1})

    def test_mixed_data_types(self):
        self.assertEqual(frequency_lists([[1, 'a', 3.5], ['a', 2], [1, 3.5]]), {1: 2, 'a': 2, 3.5: 2, 2: 1})

    def test_nested_lists(self):
        self.assertEqual(frequency_lists([[1, [2, 3]], [[4], 5]]), {1: 1, (2, 3): 1, ((4,), 5): 1})

    def test_large_list_of_lists(self):
        large_list = [[i for i in range(1000)] for _ in range(10)]
        self.assertEqual(frequency_lists(large_list)[999], 10)

    def test_special_characters(self):
        self.assertEqual(frequency_lists([['@', '#', '$'], ['@', '$']]), {'@': 2, '#': 1, '$': 2})

    def test_negative_numbers(self):
        self.assertEqual(frequency_lists([[1, -2, 3], [-2, -3], [3, -3, -2]]), {1: 1, -2: 3, 3: 2, -3: 2})

