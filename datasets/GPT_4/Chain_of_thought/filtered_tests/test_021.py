import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_021 import *

class TestVersion(unittest.TestCase):
    def test_sublist_present(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [2, 3]))

    def test_sublist_equals_list(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3]))

    def test_empty_sublist(self):
        self.assertTrue(is_sublist([1, 2, 3], []))

    def test_sublist_not_present(self):
        self.assertFalse(is_sublist([1, 2, 3, 4], [3, 5]))

    def test_sublist_longer_than_list(self):
        self.assertFalse(is_sublist([1, 2], [1, 2, 3]))

    def test_sublist_at_start(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [1, 2]))

    def test_sublist_at_end(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [4, 5]))

    def test_single_element_sublist(self):
        self.assertTrue(is_sublist([1, 2, 3, 4], [3]))

    def test_repeating_elements_in_list(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 2, 3], [2, 3]))

    def test_non_contiguous_sublist(self):
        self.assertFalse(is_sublist([1, 2, 3, 4, 5], [2, 4]))

    def test_mixed_data_types(self):
        self.assertTrue(is_sublist(['a', 1, 'b', 2], ['b', 2]))

    def test_large_list_and_sublist(self):
        self.assertTrue(is_sublist(list(range(1000000)), [999997, 999998, 999999]))

    def test_sublist_not_in_sequence(self):
        self.assertFalse(is_sublist([1, 2, 3, 4, 5], [1, 3, 5]))

