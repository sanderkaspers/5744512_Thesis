import unittest
from datasets.o3.programs.program_021 import *

class TestVersion(unittest.TestCase):
    def test_empty_sublist(self):
        self.assertTrue(is_sublist([1, 2, 3], []))

    def test_identical_lists(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3]))

    def test_sublist_at_start(self):
        self.assertTrue(is_sublist([1, 2, 3, 4], [1, 2]))

    def test_sublist_in_middle(self):
        self.assertTrue(is_sublist([5, 6, 7, 8, 9], [7, 8]))

    def test_sublist_at_end(self):
        self.assertTrue(is_sublist([10, 11, 12], [11, 12]))

    def test_not_sublist(self):
        self.assertFalse(is_sublist([1, 2, 3], [2, 4]))

    def test_longer_sublist(self):
        self.assertFalse(is_sublist([1, 2], [1, 2, 3]))

    def test_repeated_elements_true(self):
        self.assertTrue(is_sublist([1, 1, 1, 2], [1, 1]))

    def test_repeated_elements_false(self):
        self.assertFalse(is_sublist([1, 1, 2, 1], [1, 2, 1, 1]))

