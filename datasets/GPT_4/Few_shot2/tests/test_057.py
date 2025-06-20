import unittest
from datasets.GPT_4.Few_shot2.programs.program_057 import *

class TestVersion(unittest.TestCase):
    def test_common_all_identical(self): self.assertEqual(common_in_nested_lists([[1, 2], [1, 2], [1, 2]]), [1, 2])

    def test_common_some_overlap(self): self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 2]]), [2, 3])

    def test_common_no_overlap(self): self.assertEqual(common_in_nested_lists([[1, 2], [3, 4], [5, 6]]), [])

    def test_common_single_list(self): self.assertEqual(common_in_nested_lists([[1, 2, 3]]), [1, 2, 3])

    def test_common_empty_inner_list(self): self.assertEqual(common_in_nested_lists([[1, 2], [], [1]]), [])

    def test_common_all_empty(self): self.assertEqual(common_in_nested_lists([[], [], []]), [])

    def test_common_nested_with_duplicates(self): self.assertEqual(common_in_nested_lists([[1, 1, 2], [2, 2, 1], [1, 2]]), [1, 2])

    def test_common_nested_single_element_overlap(self): self.assertEqual(common_in_nested_lists([[9], [9, 10], [9, 11]]), [9])

