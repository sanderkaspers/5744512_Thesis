import unittest
from datasets.GPT_4.Few_shot2.programs.program_017 import *

class TestVersion(unittest.TestCase):
    def test_recursive_list_sum_flat_list(self): self.assertEqual(recursive_list_sum([1, 2, 3]), 6)

    def test_recursive_list_sum_nested_list(self): self.assertEqual(recursive_list_sum([1, [2, 3], 4]), 10)

    def test_recursive_list_sum_deeply_nested(self): self.assertEqual(recursive_list_sum([1, [2, [3, [4]]]]), 10)

    def test_recursive_list_sum_empty_list(self): self.assertEqual(recursive_list_sum([]), 0)

    def test_recursive_list_sum_empty_nested_lists(self): self.assertEqual(recursive_list_sum([[], [[]], [[[]]]]), 0)

    def test_recursive_list_sum_negative_numbers(self): self.assertEqual(recursive_list_sum([-1, [-2, -3]]), -6)

    def test_recursive_list_sum_zero(self): self.assertEqual(recursive_list_sum([0, [0, 0]]), 0)

    def test_recursive_list_sum_large_values(self): self.assertEqual(recursive_list_sum([1000, [2000, [3000]]]), 6000)

    def test_recursive_list_sum_single_element_nested(self): self.assertEqual(recursive_list_sum([[5]]), 5)

    def test_recursive_list_sum_mixed_depths(self): self.assertEqual(recursive_list_sum([1, [2], [3, [4, [5]]]]), 15)

