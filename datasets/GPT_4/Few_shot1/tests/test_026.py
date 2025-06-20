import unittest
from datasets.GPT_4.Few_shot1.programs.program_026 import *

class TestVersion(unittest.TestCase):
    def test_find_tuples_exact_match(self): self.assertEqual(find_tuples([(1, 2), (3,), (4, 5)], 2), [(1, 2), (4, 5)])

    def test_find_tuples_no_match(self): self.assertEqual(find_tuples([(1,), (2,), (3,)], 3), [])

    def test_find_tuples_all_match(self): self.assertEqual(find_tuples([(1,), (2,), (3,)], 1), [(1,), (2,), (3,)])

    def test_find_tuples_empty_input(self): self.assertEqual(find_tuples([], 2), [])

    def test_find_tuples_zero_length(self): self.assertEqual(find_tuples([(), (1,), (1,2)], 0), [()])

    def test_find_tuples_large_K(self): self.assertEqual(find_tuples([(1,2,3), (4,5), (6,7,8,9)], 4), [(6,7,8,9)])

    def test_find_tuples_mixed_lengths(self): self.assertEqual(find_tuples([(1,), (2,3), (4,5,6)], 3), [(4,5,6)])

    def test_find_tuples_with_non_tuples(self): self.assertEqual(find_tuples([(1,2), [3,4], (5,6)], 2), [(1,2), (5,6)])

    def test_find_tuples_strings_in_tuples(self): self.assertEqual(find_tuples([("a", "b"), ("x",), ("a", "b", "c")], 2), [("a", "b")])

    def test_find_tuples_invalid_tuple_format(self): self.assertEqual(find_tuples(["not a tuple", (1, 2)], 2), [(1, 2)])

