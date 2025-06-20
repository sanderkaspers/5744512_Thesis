import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_054 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))

    def test_empty_list(self):
        self.assertEqual(add_lists([], (4, 5, 6)), (4, 5, 6))

    def test_empty_tuple(self):
        self.assertEqual(add_lists([1, 2, 3], ()), (1, 2, 3))

    def test_both_empty(self):
        self.assertEqual(add_lists([], ()), ())

    def test_list_with_mixed_data_types(self):
        self.assertEqual(add_lists([1, 'a', 3.5], (4, 'b', 6.7)), (4, 'b', 6.7, 1, 'a', 3.5))

    def test_tuple_with_mixed_data_types(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 'b', 6.7)), (4, 'b', 6.7, 1, 2, 3))

    def test_nested_lists(self):
        self.assertEqual(add_lists([[1, 2], [3, 4]], (5, 6)), (5, 6, [1, 2], [3, 4]))

    def test_nested_tuples(self):
        self.assertEqual(add_lists([1, 2], ((3, 4), 5)), ((3, 4), 5, 1, 2))

    def test_large_list_and_tuple(self):
        large_list = list(range(1000))
        large_tuple = tuple(range(1000, 2000))
        self.assertEqual(add_lists(large_list, large_tuple), tuple(range(1000, 2000)) + tuple(range(1000)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            add_lists('string', (1, 2))
        with self.assertRaises(TypeError):
            add_lists([1, 2], 'string')

