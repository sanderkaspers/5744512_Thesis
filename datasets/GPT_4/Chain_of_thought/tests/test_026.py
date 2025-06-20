import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_026 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_tuples([(2, 4), (3, 6), (8, 10)], 2), [(2, 4), (8, 10)])

    def test_no_tuples_matching(self):
        self.assertEqual(find_tuples([(1, 3), (7, 11)], 2), [])

    def test_all_tuples_matching(self):
        self.assertEqual(find_tuples([(4, 8), (2, 6)], 2), [(4, 8), (2, 6)])

    def test_single_tuple_matching(self):
        self.assertEqual(find_tuples([(6, 12)], 3), [(6, 12)])

    def test_single_tuple_non_matching(self):
        self.assertEqual(find_tuples([(5, 7)], 3), [])

    def test_empty_list(self):
        self.assertEqual(find_tuples([], 3), [])

    def test_empty_tuples(self):
        self.assertEqual(find_tuples([(), ()], 3), [(), ()])

    def test_large_K_value(self):
        self.assertEqual(find_tuples([(10, 20), (30, 40)], 1000), [])

    def test_negative_numbers(self):
        self.assertEqual(find_tuples([(-2, -4), (-3, -6)], 2), [(-2, -4)])

    def test_mixed_positive_negative(self):
        self.assertEqual(find_tuples([(2, -4), (3, 9)], 2), [(2, -4)])

    def test_zero_as_K(self):
        with self.assertRaises(ZeroDivisionError):
            find_tuples([(2, 4), (3, 6)], 0)

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            find_tuples([(2, 'a'), (3, 6)], 2)

    def test_floating_point_numbers(self):
        self.assertEqual(find_tuples([(2.0, 4.0), (3.0, 6.0)], 2), [(2.0, 4.0)])

