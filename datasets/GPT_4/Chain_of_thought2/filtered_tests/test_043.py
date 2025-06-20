import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_043 import *

class TestVersion(unittest.TestCase):
    def test_varied_lengths(self): self.assertEqual(Find_Min_Length([[1, 2], [3], [4, 5, 6]]), 1)

    def test_same_length_lists(self): self.assertEqual(Find_Min_Length([[1], [2], [3]]), 1)

    def test_single_list(self): self.assertEqual(Find_Min_Length([[1, 2, 3, 4]]), 4)

    def test_contains_empty_list(self): self.assertEqual(Find_Min_Length([[1, 2], [], [3, 4, 5]]), 0)

    def test_all_empty_lists(self): self.assertEqual(Find_Min_Length([[], [], []]), 0)

    def test_inner_elements_are_strings(self): self.assertEqual(Find_Min_Length([["hi"], ["hello", "world"], ["a"]]), 1)

    def test_inner_elements_are_tuples(self): self.assertEqual(Find_Min_Length([(1, 2), (3,), (4, 5, 6)]), 1)

    def test_mixed_iterable_inner_elements(self): self.assertEqual(Find_Min_Length([[1, 2], (3, 4), "abc"]), 2)

