import unittest
from datasets.GPT_4.Few_shot1.programs.program_017 import *

class TestVersion(unittest.TestCase):
    def test_recursive_list_sum_flat_list(self): self.assertEqual(recursive_list_sum([1, 2, 3]), 6)

    def test_recursive_list_sum_nested_list(self): self.assertEqual(recursive_list_sum([1, [2, 3]]), 6)

    def test_recursive_list_sum_deeply_nested(self): self.assertEqual(recursive_list_sum([1, [2, [3, [4]]]]), 10)

    def test_recursive_list_sum_with_zeros(self): self.assertEqual(recursive_list_sum([0, [0, [0]]]), 0)

    def test_recursive_list_sum_with_negatives(self): self.assertEqual(recursive_list_sum([-1, [-2, [-3]]]), -6)

    def test_recursive_list_sum_empty_list(self): self.assertEqual(recursive_list_sum([]), 0)

    def test_recursive_list_sum_nested_empty_lists(self): self.assertEqual(recursive_list_sum([[], [[]], [[[]]]]), 0)

    def test_recursive_list_sum_large_numbers(self): self.assertEqual(recursive_list_sum([1000000, [2000000]]), 3000000)

    def test_recursive_list_sum_single_nested_value(self): self.assertEqual(recursive_list_sum([[42]]), 42)

