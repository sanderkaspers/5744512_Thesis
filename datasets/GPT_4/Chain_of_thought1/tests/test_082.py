import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_082 import *

class TestVersion(unittest.TestCase):
    def test_all_same(self): self.assertEqual(count_samepair([1, 1], [1, 1], [1, 1]), 2)

    def test_all_distinct(self): self.assertEqual(count_samepair([1, 2], [3, 4], [5, 6]), 0)

    def test_single_match(self): self.assertEqual(count_samepair([1, 2], [1, 3], [1, 4]), 1)

    def test_partial_match(self): self.assertEqual(count_samepair([1, 2, 3], [1, 5, 3], [1, 6, 3]), 2)

    def test_different_lengths(self): self.assertEqual(count_samepair([1, 2], [1], [1, 2, 3]), 1)

    def test_single_element(self): self.assertEqual(count_samepair([5], [5], [5]), 1)

    def test_empty_lists(self): self.assertEqual(count_samepair([], [], []), 0)

    def test_equal_but_different_types(self): self.assertEqual(count_samepair([1], [1.0], [True]), 1)

    def test_mixed_types(self): self.assertEqual(count_samepair([1], ['1'], [1]), 0)

    def test_with_none(self): self.assertEqual(count_samepair([None, 1], [None, 2], [None, 1]), 1)

    def test_nested_lists(self): a = [1, 2]; self.assertEqual(count_samepair([a], [a], [a]), 1)

