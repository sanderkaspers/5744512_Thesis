import unittest
from datasets.o3.programs.program_042 import *

class TestVersion(unittest.TestCase):
    def test_single_tuple(self):
        self.assertEqual(first_of_min_second([(5, 1)]), 5)

    def test_two_tuples(self):
        self.assertEqual(first_of_min_second([(1, 3), (2, 1)]), 2)

    def test_multiple_min_values(self):
        self.assertEqual(first_of_min_second([(7, 2), (8, 2), (1, 5)]), 7)

    def test_negative_numbers(self):
        self.assertEqual(first_of_min_second([(-1, -5), (-2, -3)]), -1)

    def test_string_first_elements(self):
        self.assertEqual(first_of_min_second([('a', 10), ('b', 2)]), 'b')

    def test_empty_pairs_raises(self):
        with self.assertRaises(ValueError):
            first_of_min_second([])

