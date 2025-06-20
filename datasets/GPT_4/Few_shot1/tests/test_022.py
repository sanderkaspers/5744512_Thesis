import unittest
from datasets.GPT_4.Few_shot1.programs.program_022 import *

class TestVersion(unittest.TestCase):
    def test_find_equal_tuple_one_match(self): self.assertEqual(find_equal_tuple([(1, 1), (2, 3)]), [1, 1])

    def test_find_equal_tuple_first_match(self): self.assertEqual(find_equal_tuple([(9, 9, 9), (5, 5, 4)]), [9, 9, 9])

    def test_find_equal_tuple_later_match(self): self.assertEqual(find_equal_tuple([(1, 2), (3, 3), (4, 4, 4)]), [3, 3])

    def test_find_equal_tuple_no_match(self): self.assertEqual(find_equal_tuple([(1, 2), (3, 4), (5, 6)]), [])

    def test_find_equal_tuple_empty_input(self): self.assertEqual(find_equal_tuple([]), [])

    def test_find_equal_tuple_single_element_tuples(self): self.assertEqual(find_equal_tuple([(1,), (2,)]), [1])

    def test_find_equal_tuple_nested_same_and_different(self): self.assertEqual(find_equal_tuple([(1, 1, 1), (2, 2), (2, 3)]), [1, 1, 1])

    def test_find_equal_tuple_strings(self): self.assertEqual(find_equal_tuple([("a", "a"), ("b", "c")]), ["a", "a"])

    def test_find_equal_tuple_all_invalid_lengths(self): self.assertEqual(find_equal_tuple([(1,), (2, 3, 4), (5, 6)]), [1])

    def test_find_equal_tuple_multiple_valid(self): self.assertEqual(find_equal_tuple([(8, 8), (9, 9, 9), (10, 10)]), [8, 8])

