import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_036 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(freq_count([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})

    def test_all_unique_elements(self):
        self.assertEqual(freq_count([1, 2, 3, 4]), {1: 1, 2: 1, 3: 1, 4: 1})

    def test_all_identical_elements(self):
        self.assertEqual(freq_count([2, 2, 2, 2]), {2: 4})

    def test_empty_list(self):
        self.assertEqual(freq_count([]), {})

    def test_mixed_data_types(self):
        self.assertEqual(freq_count([1, 'a', 1, 'b', 'a']), {1: 2, 'a': 2, 'b': 1})

    def test_single_element(self):
        self.assertEqual(freq_count([99]), {99: 1})

    def test_large_list(self):
        large_list = [i % 10 for i in range(1000)]
        expected = {i: 100 for i in range(10)}
        self.assertEqual(freq_count(large_list), expected)

    def test_nested_lists(self):
        with self.assertRaises(TypeError):
            freq_count([[1, 2], [1, 2]])

    def test_non_numeric_elements(self):
        self.assertEqual(freq_count(['apple', 'banana', 'apple', 'orange', 'banana']), {'apple': 2, 'banana': 2, 'orange': 1})

    def test_boundary_values(self):
        self.assertEqual(freq_count([2147483647, -2147483648, 2147483647]), {2147483647: 2, -2147483648: 1})

