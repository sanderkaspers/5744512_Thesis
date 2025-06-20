import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_017 import *

class TestVersion(unittest.TestCase):
    def test_flat_list(self): self.assertEqual(recursive_list_sum([1, 2, 3]), 6)

    def test_single_nested_list(self): self.assertEqual(recursive_list_sum([1, [2, 3], 4]), 10)

    def test_deeply_nested_list(self): self.assertEqual(recursive_list_sum([1, [2, [3, [4]]]]), 10)

    def test_mixed_nested(self): self.assertEqual(recursive_list_sum([1, [2], 3, [4, [5]]]), 15)

    def test_empty_list(self): self.assertEqual(recursive_list_sum([]), 0)

    def test_list_of_empty_lists(self): self.assertEqual(recursive_list_sum([[], [], []]), 0)

    def test_nested_empty_lists(self): self.assertEqual(recursive_list_sum([[[[]]]]), 0)

    def test_list_with_floats(self): self.assertEqual(recursive_list_sum([1.5, [2.5, 3]]), 7.0)

    def test_list_with_booleans(self): self.assertEqual(recursive_list_sum([True, False, 1]), 2)

    def test_numeric_nested_only(self): self.assertEqual(recursive_list_sum([[1], [[2]], [[[3]]]]), 6)

