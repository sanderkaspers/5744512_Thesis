import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_054 import *

class TestVersion(unittest.TestCase):
    def test_normal_case(self): self.assertEqual(add_lists([1, 2], (3, 4)), [1, 2, 3, 4])

    def test_empty_list(self): self.assertEqual(add_lists([], (1, 2)), [1, 2])

    def test_empty_tuple(self): self.assertEqual(add_lists([1, 2], ()), [1, 2])

    def test_both_empty(self): self.assertEqual(add_lists([], ()), [])

    def test_unequal_lengths(self): self.assertEqual(add_lists([1], (2, 3, 4)), [1, 2, 3, 4])

    def test_negatives(self): self.assertEqual(add_lists([-1, -2], (-3, -4)), [-1, -2, -3, -4])

    def test_floats(self): self.assertEqual(add_lists([1.1, 2.2], (3.3, 4.4)), [1.1, 2.2, 3.3, 4.4])

    def test_mixed_types(self): self.assertEqual(add_lists([1, 'a'], ('b', 2)), [1, 'a', 'b', 2])

    def test_nested(self): self.assertEqual(add_lists([[1], [2]], ([3], [4])), [[1], [2], [3], [4]])

    def test_tuple_with_none(self): self.assertEqual(add_lists([1], (None, 2)), [1, None, 2])

