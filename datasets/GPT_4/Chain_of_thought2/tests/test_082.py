import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_082 import *

class TestVersion(unittest.TestCase):
    def test_all_match(self): self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)

    def test_none_match(self): self.assertEqual(count_samepair([1, 2], [3, 4], [5, 6]), 0)

    def test_some_match(self): self.assertEqual(count_samepair([1, 2, 3], [1, 4, 3], [1, 5, 3]), 2)

    def test_unequal_length_lists(self): self.assertEqual(count_samepair([1, 2, 3, 4], [1, 2], [1, 2, 3]), 2)

    def test_empty_lists(self): self.assertEqual(count_samepair([], [], []), 0)

    def test_single_element_all_match(self): self.assertEqual(count_samepair([9], [9], [9]), 1)

    def test_single_element_none_match(self): self.assertEqual(count_samepair([1], [2], [3]), 0)

    def test_mixed_data_types(self): self.assertEqual(count_samepair([1, 'a'], [1, 'a'], [1, 'a']), 2)

    def test_case_sensitive_strings(self): self.assertEqual(count_samepair(['A', 'b'], ['a', 'b'], ['A', 'B']), 1)

    def test_lists_with_none(self): self.assertEqual(count_samepair([None, 2], [None, 3], [None, 4]), 1)

