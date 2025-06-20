import unittest
from datasets.GPT_4.Few_shot1.programs.program_093 import *

class TestVersion(unittest.TestCase):
    def test_frequency_basic_match(self): self.assertEqual(frequency([1, 2, 3, 2, 2], 2), 3)

    def test_frequency_no_match(self): self.assertEqual(frequency([1, 2, 3], 4), 0)

    def test_frequency_all_match(self): self.assertEqual(frequency([5, 5, 5, 5], 5), 4)

    def test_frequency_empty_list(self): self.assertEqual(frequency([], 1), 0)

    def test_frequency_single_element_match(self): self.assertEqual(frequency([7], 7), 1)

    def test_frequency_single_element_no_match(self): self.assertEqual(frequency([7], 3), 0)

    def test_frequency_mixed_types(self): self.assertEqual(frequency([1, '1', 1.0], 1), 2)

    def test_frequency_strings(self): self.assertEqual(frequency(['a', 'b', 'a'], 'a'), 2)

    def test_frequency_case_sensitive(self): self.assertEqual(frequency(['A', 'a'], 'a'), 1)

    def test_frequency_nested_lists(self): self.assertEqual(frequency([[1], [1], 1], [1]), 2)

    def test_frequency_none_values(self): self.assertEqual(frequency([None, 1, None], None), 2)

    def test_frequency_booleans(self): self.assertEqual(frequency([True, False, True, 1], True), 3)

    def test_frequency_large_list(self): self.assertEqual(frequency([0]*1000 + [1]*500, 1), 500)

    def test_frequency_negative_values(self): self.assertEqual(frequency([-1, -2, -1, 0], -1), 2)

    def test_frequency_float_comparison(self): self.assertEqual(frequency([1.0, 2.0, 1.0], 1), 2)

