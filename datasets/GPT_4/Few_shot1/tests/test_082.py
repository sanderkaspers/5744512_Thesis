import unittest
from datasets.GPT_4.Few_shot1.programs.program_082 import *

class TestVersion(unittest.TestCase):
    def test_count_samepair_all_match(self): self.assertEqual(count_samepair([1, 2], [1, 2], [1, 2]), 2)

    def test_count_samepair_none_match(self): self.assertEqual(count_samepair([1, 2], [3, 4], [5, 6]), 0)

    def test_count_samepair_partial_match(self): self.assertEqual(count_samepair([1, 2], [1, 3], [1, 4]), 1)

    def test_count_samepair_empty_lists(self): self.assertEqual(count_samepair([], [], []), 0)

    def test_count_samepair_single_element_match(self): self.assertEqual(count_samepair([7], [7], [7]), 1)

    def test_count_samepair_single_element_no_match(self): self.assertEqual(count_samepair([1], [2], [3]), 0)

    def test_count_samepair_mixed_types(self): self.assertEqual(count_samepair(["a", 1], ["a", 2], ["a", 3]), 1)

    def test_count_samepair_lists_of_different_lengths(self): self.assertEqual(count_samepair([1, 2, 3], [1, 2], [1]), 1)

    def test_count_samepair_repeated_values(self): self.assertEqual(count_samepair([2, 2, 2], [2, 2, 3], [2, 2, 2]), 2)

    def test_count_samepair_large_input(self): self.assertEqual(count_samepair([1]*1000, [1]*1000, [1]*1000), 1000)

