import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_061 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(list_to_float([['1', '2'], ['3.5', '4.2']]), [(1.0, 2.0), (3.5, 4.2)])

    def test_mixed_data_types(self):
        self.assertEqual(list_to_float([['1', 'a'], ['b', '3.5']]), [(1.0, 'a'), ('b', 3.5)])

    def test_empty_list(self):
        self.assertEqual(list_to_float([]), [])

    def test_non_convertible_elements(self):
        with self.assertRaises(ValueError):
            list_to_float([['a', 'b'], ['c', 'd']])

    def test_nested_lists(self):
        with self.assertRaises(IndexError):
            list_to_float([['1', ['2', '3']], ['4', '5']])

    def test_integers_and_floats(self):
        self.assertEqual(list_to_float([['10', '20'], ['30.5', '40.2']]), [(10.0, 20.0), (30.5, 40.2)])

    def test_special_characters(self):
        with self.assertRaises(ValueError):
            list_to_float([['1@', '2#'], ['3$', '4%']])

    def test_negative_numbers(self):
        self.assertEqual(list_to_float([['-1', '-2'], ['-3.5', '-4.2']]), [(-1.0, -2.0), (-3.5, -4.2)])

    def test_strings_that_look_like_numbers(self):
        with self.assertRaises(ValueError):
            list_to_float([['123abc', '456def'], ['789ghi', '012jkl']])

    def test_very_large_numbers(self):
        self.assertEqual(list_to_float([['1e10', '2e20'], ['3e30', '4e40']]), [(1e10, 2e20), (3e30, 4e40)])

