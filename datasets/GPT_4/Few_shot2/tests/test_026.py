import unittest
from datasets.GPT_4.Few_shot2.programs.program_026 import *

class TestVersion(unittest.TestCase):
    def test_find_tuples_basic(self): self.assertEqual(find_tuples([(1,), (2, 3), (4, 5, 6)], 2), [(2, 3)])

    def test_find_tuples_all_match(self): self.assertEqual(find_tuples([(1, 2), (3, 4)], 2), [(1, 2), (3, 4)])

    def test_find_tuples_none_match(self): self.assertEqual(find_tuples([(1,), (2, 3, 4)], 2), [])

    def test_find_tuples_empty_list(self): self.assertEqual(find_tuples([], 1), [])

    def test_find_tuples_k_zero(self): self.assertEqual(find_tuples([((),), (1,)], 0), [])

    def test_find_tuples_with_empty_tuple(self): self.assertEqual(find_tuples([(), (1,), (2, 3)], 0), [()])

    def test_find_tuples_k_greater_than_any(self): self.assertEqual(find_tuples([(1,), (2, 3)], 5), [])

    def test_find_tuples_single_element(self): self.assertEqual(find_tuples([(1, 2)], 2), [(1, 2)])

    def test_find_tuples_multiple_matches(self): self.assertEqual(find_tuples([(1,), (2,), (3,)], 1), [(1,), (2,), (3,)])

    def test_find_tuples_nested_tuple(self): self.assertEqual(find_tuples([((1, 2),), (3, 4)], 1), [((1, 2),)])

