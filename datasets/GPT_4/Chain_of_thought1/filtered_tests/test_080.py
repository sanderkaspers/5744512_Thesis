import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_080 import *

class TestVersion(unittest.TestCase):
    def test_mixed_elements(self): self.assertEqual(extract_singly([[1, 2], [2, 3], [4]]), [1, 2, 3, 4])

    def test_all_distinct(self): self.assertEqual(extract_singly([[1], [2], [3]]), [1, 2, 3])

    def test_all_empty_inner(self): self.assertEqual(extract_singly([[], [], []]), [])

    def test_duplicates_in_inner(self): self.assertEqual(extract_singly([[1, 1], [2]]), [1, 2])

    def test_all_same(self): self.assertEqual(extract_singly([[1], [1], [1]]), [1])

    def test_mixed_types(self): self.assertEqual(extract_singly([[1, 'a'], ['a', 2]]), [1, 'a', 2])

    def test_single_inner(self): self.assertEqual(extract_singly([[4, 5, 4]]), [4, 5])

    def test_empty_outer_list(self): self.assertEqual(extract_singly([]), [])

