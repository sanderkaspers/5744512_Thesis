import unittest
from datasets.GPT_4.Few_shot1.programs.program_057 import *

class TestVersion(unittest.TestCase):
    def test_common_basic(self): self.assertEqual(sorted(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 2]])), [2, 3])

    def test_common_none(self): self.assertEqual(common_in_nested_lists([[1, 2], [3, 4]]), [])

    def test_common_single_list(self): self.assertEqual(sorted(common_in_nested_lists([[5, 6, 7]])), [5, 6, 7])

    def test_common_empty_nested(self): self.assertEqual(common_in_nested_lists([[]]), [])

    def test_common_one_empty(self): self.assertEqual(common_in_nested_lists([[1, 2], []]), [])

    def test_common_identical_lists(self): self.assertEqual(sorted(common_in_nested_lists([[1, 2], [1, 2], [1, 2]])), [1, 2])

    def test_common_with_duplicates(self): self.assertEqual(sorted(common_in_nested_lists([[1, 1, 2], [1, 2, 2], [1, 2]])), [1, 2])

