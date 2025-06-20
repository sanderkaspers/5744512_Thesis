import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_080 import *

class TestVersion(unittest.TestCase):
    def test_all_unique(self): self.assertEqual(extract_singly([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_duplicates_across_lists(self): self.assertEqual(extract_singly([[1, 2], [2, 3], [3, 4]]), [1, 2, 3, 4])

    def test_duplicates_within_list(self): self.assertEqual(extract_singly([[1, 1], [2, 2]]), [1, 2])

    def test_single_inner_list(self): self.assertEqual(extract_singly([[5, 6, 7]]), [5, 6, 7])

    def test_empty_outer_list(self): self.assertEqual(extract_singly([]), [])

    def test_empty_inner_lists(self): self.assertEqual(extract_singly([[], [], []]), [])

    def test_some_empty_inner_lists(self): self.assertEqual(extract_singly([[1, 2], [], [2, 3]]), [1, 2, 3])

    def test_all_elements_same(self): self.assertEqual(extract_singly([[9, 9], [9], [9, 9]]), [9])

    def test_non_integer_elements(self): self.assertEqual(extract_singly([['a', 'b'], ['b', 'c']]), ['a', 'b', 'c'])

    def test_floats_and_integers(self): self.assertEqual(extract_singly([[1.1, 2.2], [1.1, 3.3]]), [1.1, 2.2, 3.3])

    def test_large_nested_list(self): self.assertEqual(extract_singly([[i, i+1] for i in range(0, 100, 2)]), list(range(0, 101)))

    def test_mixed_hashable_types(self): self.assertEqual(extract_singly([[1, '1'], [1, '1']]), [1, '1'])

