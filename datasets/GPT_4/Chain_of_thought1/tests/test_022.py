import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_022 import *

class TestVersion(unittest.TestCase):
    def test_no_duplicates(self): self.assertEqual(find_equal_tuple([1, 2, 3]), ())

    def test_first_two_equal(self): self.assertEqual(find_equal_tuple([5, 5, 1]), (5, 5))

    def test_match_in_middle(self): self.assertEqual(find_equal_tuple([1, 2, 3, 2]), (2, 2))

    def test_match_at_end(self): self.assertEqual(find_equal_tuple([4, 5, 6, 4]), (4, 4))

    def test_multiple_duplicates(self): self.assertEqual(find_equal_tuple([1, 2, 3, 2, 3]), (2, 2))

    def test_all_same(self): self.assertEqual(find_equal_tuple([7, 7, 7]), (7, 7))

    def test_empty_list(self): self.assertEqual(find_equal_tuple([]), ())

    def test_single_element(self): self.assertEqual(find_equal_tuple([1]), ())

    def test_boolean_values(self): self.assertEqual(find_equal_tuple([True, False, True]), (True, True))

    def test_string_duplicates(self): self.assertEqual(find_equal_tuple(['apple', 'banana', 'apple']), ('apple', 'apple'))

    def test_int_float_equivalence(self): self.assertEqual(find_equal_tuple([1, 1.0]), (1, 1))

