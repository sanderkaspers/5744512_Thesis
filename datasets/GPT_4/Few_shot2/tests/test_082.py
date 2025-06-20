import unittest
from datasets.GPT_4.Few_shot2.programs.program_082 import *

class TestVersion(unittest.TestCase):
    def test_count_samepair_all_match(self): self.assertEqual(count_samepair([1, 2], [1, 2], [1, 2]), 2)

    def test_count_samepair_none_match(self): self.assertEqual(count_samepair([1, 2], [3, 4], [5, 6]), 0)

    def test_count_samepair_partial_match(self): self.assertEqual(count_samepair([1, 2, 3], [1, 5, 3], [1, 5, 0]), 1)

    def test_count_samepair_empty_lists(self): self.assertEqual(count_samepair([], [], []), 0)

    def test_count_samepair_single_element_match(self): self.assertEqual(count_samepair([5], [5], [5]), 1)

    def test_count_samepair_single_element_no_match(self): self.assertEqual(count_samepair([1], [2], [3]), 0)

    def test_count_samepair_mixed_types(self): self.assertEqual(count_samepair(['a', 2, 3.0], ['a', 2.0, 3], ['a', 2, 3.0]), 1)

    def test_count_samepair_more_elements_ignored(self): self.assertEqual(count_samepair([1, 1, 1], [1, 2], [1, 2, 3]), 1)

