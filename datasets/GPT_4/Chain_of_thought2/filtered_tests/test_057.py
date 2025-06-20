import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_057 import *

class TestVersion(unittest.TestCase):
    def test_single_common_element(self): self.assertEqual(sorted(common_in_nested_lists([[1, 2], [2, 3], [2, 4]])), [2])

    def test_multiple_common_elements(self): self.assertEqual(sorted(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [2, 3, 5]])), [2, 3])

    def test_identical_sublists(self): self.assertEqual(sorted(common_in_nested_lists([[1, 2], [1, 2], [1, 2]])), [1, 2])

    def test_only_one_sublist(self): self.assertEqual(sorted(common_in_nested_lists([[1, 2, 3]])), [1, 2, 3])

    def test_one_empty_sublist(self): self.assertEqual(common_in_nested_lists([[1, 2], [], [1, 2]]), [])

    def test_all_empty_sublists(self): self.assertEqual(common_in_nested_lists([[], [], []]), [])

    def test_no_common_elements(self): self.assertEqual(common_in_nested_lists([[1], [2], [3]]), [])

    def test_with_duplicates(self): self.assertEqual(sorted(common_in_nested_lists([[1, 1, 2], [1, 3, 1], [1, 4]])), [1])

    def test_mixed_data_types(self): self.assertEqual(sorted(common_in_nested_lists([[1, 'a'], ['a', 2], ['a', 3]])), ['a'])

