import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_093 import *

class TestVersion(unittest.TestCase):
    def test_multiple_occurrences(self): self.assertEqual(frequency([1, 2, 2, 3, 2], 2), 3)

    def test_single_occurrence(self): self.assertEqual(frequency([5, 6, 7], 6), 1)

    def test_no_occurrence(self): self.assertEqual(frequency([8, 9, 10], 7), 0)

    def test_all_same_elements(self): self.assertEqual(frequency([4, 4, 4, 4], 4), 4)

    def test_empty_list(self): self.assertEqual(frequency([], 1), 0)

    def test_search_none(self): self.assertEqual(frequency([None, 1, None, 2], None), 2)

    def test_mixed_types(self): self.assertEqual(frequency([1, '1', 1.0], 1), 2)

    def test_search_string(self): self.assertEqual(frequency(['a', 'b', 'a', 'c'], 'a'), 2)

    def test_list_with_one_match(self): self.assertEqual(frequency([5], 5), 1)

    def test_list_with_one_no_match(self): self.assertEqual(frequency([5], 4), 0)

