import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_057 import *

class TestVersion(unittest.TestCase):
    def test_partial_overlap(self): result = common_in_nested_lists([[1, 2, 3], [2, 3], [3, 2, 4]]); self.assertCountEqual(result, [2, 3])

    def test_all_identical(self): result = common_in_nested_lists([[1, 2], [1, 2], [1, 2]]); self.assertCountEqual(result, [1, 2])

    def test_no_common_elements(self): self.assertEqual(common_in_nested_lists([[1, 2], [3, 4], [5]]), [])

    def test_single_list(self): result = common_in_nested_lists([[10, 20]]); self.assertCountEqual(result, [10, 20])

    def test_varying_lengths(self): result = common_in_nested_lists([[1, 2, 3], [2], [2, 4, 5]]); self.assertEqual(result, [2])

    def test_duplicates_in_sublists(self): result = common_in_nested_lists([[1, 1, 2], [1, 3], [1]]); self.assertEqual(result, [1])

    def test_different_types(self): self.assertEqual(common_in_nested_lists([[1, 'a'], [1, 'a'], [1]]), [1])

    def test_empty_sublist(self): self.assertEqual(common_in_nested_lists([[1, 2], [], [1, 2]]), [])

    def test_common_zero(self): self.assertEqual(common_in_nested_lists([[0, 1], [0, 2], [0]]), [0])

    def test_type_conflict(self): self.assertEqual(common_in_nested_lists([[1, '1'], [1], [1, 2]]), [1])

