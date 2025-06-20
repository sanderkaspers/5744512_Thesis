import unittest
from datasets.GPT_4.Few_shot1.programs.program_080 import *

class TestVersion(unittest.TestCase):
    def test_extract_singly_basic(self): self.assertEqual(extract_singly([[1, 2], [2, 3]]), [1, 2, 3])

    def test_extract_singly_single_list(self): self.assertEqual(extract_singly([[1, 2, 3]]), [1, 2, 3])

    def test_extract_singly_duplicates_in_list(self): self.assertEqual(extract_singly([[1, 1], [1, 1]]), [1])

    def test_extract_singly_all_unique(self): self.assertEqual(extract_singly([[1], [2], [3]]), [1, 2, 3])

    def test_extract_singly_empty_inner_lists(self): self.assertEqual(extract_singly([[], [], []]), [])

    def test_extract_singly_empty_outer_list(self): self.assertEqual(extract_singly([]), [])

    def test_extract_singly_mixed_duplicates(self): self.assertEqual(extract_singly([[4, 5], [5, 6], [4, 7]]), [4, 5, 6, 7])

    def test_extract_singly_nested_single_elements(self): self.assertEqual(extract_singly([[1], [1], [2]]), [1, 2])

    def test_extract_singly_strings(self): self.assertEqual(extract_singly([["a", "b"], ["a", "c"]]), ["a", "b", "c"])

    def test_extract_singly_large_input(self): self.assertEqual(extract_singly([[i for i in range(100)], [50, 150]]), list(range(100)) + [150])

