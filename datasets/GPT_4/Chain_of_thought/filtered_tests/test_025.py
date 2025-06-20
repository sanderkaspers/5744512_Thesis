import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_025 import *

class TestVersion(unittest.TestCase):
    def test_typical_case_matching(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'red'], ['a', 'b', 'a']))

    def test_mismatched_lengths(self):
        self.assertFalse(is_samepatterns(['red', 'blue'], ['a', 'b', 'a']))

    def test_patterns_not_matching(self):
        self.assertFalse(is_samepatterns(['red', 'blue', 'green'], ['a', 'a', 'b']))

    def test_repeated_patterns(self):
        self.assertTrue(is_samepatterns(['red', 'red', 'blue'], ['a', 'a', 'b']))

    def test_single_element_lists(self):
        self.assertTrue(is_samepatterns(['red'], ['a']))

    def test_empty_lists(self):
        self.assertTrue(is_samepatterns([], []))

    def test_patterns_unique_elements(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'green'], ['a', 'b', 'c']))

    def test_patterns_identical_elements(self):
        self.assertTrue(is_samepatterns(['red', 'red', 'red'], ['a', 'a', 'a']))

    def test_colors_identical_elements(self):
        self.assertFalse(is_samepatterns(['red', 'red', 'red'], ['a', 'b', 'c']))

    def test_mixed_data_types(self):
        self.assertTrue(is_samepatterns([1, 2, 1], ['a', 'b', 'a']))

    def test_patterns_subset_of_colors(self):
        self.assertFalse(is_samepatterns(['red', 'blue', 'red', 'green'], ['a', 'b', 'a']))

    def test_boundary_values_large_sequences(self):
        colors = ['red'] * 1000 + ['blue'] * 1000
        patterns = ['a'] * 1000 + ['b'] * 1000
        self.assertTrue(is_samepatterns(colors, patterns))

