import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_042 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(index_minimum([(1, 10), (2, 5), (3, 20)]), 2)

    def test_multiple_same_second_value(self):
        self.assertEqual(index_minimum([(1, 5), (2, 5), (3, 10)]), 1)

    def test_single_tuple(self):
        self.assertEqual(index_minimum([(1, 100)]), 1)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            index_minimum([])

    def test_negative_positive_values(self):
        self.assertEqual(index_minimum([(1, -10), (2, 5), (3, -20)]), 3)

    def test_all_same_second_value(self):
        self.assertEqual(index_minimum([(1, 5), (2, 5), (3, 5)]), 1)

    def test_floats_in_tuple(self):
        self.assertEqual(index_minimum([(1, 1.5), (2, 0.5), (3, 2.5)]), 2)

    def test_large_list(self):
        large_list = [(i, i) for i in range(1000)]
        self.assertEqual(index_minimum(large_list), 0)

    def test_complex_objects_in_tuple(self):
        with self.assertRaises(TypeError):
            index_minimum([(1, [1, 2]), (2, [2, 3])])

