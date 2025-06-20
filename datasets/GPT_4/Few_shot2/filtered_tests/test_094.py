import unittest
from datasets.GPT_4.Few_shot2.programs.program_094 import *

class TestVersion(unittest.TestCase):
    def test_sum_range_list_normal_range(self): self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 9)

    def test_sum_range_list_full_range(self): self.assertEqual(sum_range_list([1, 2, 3], 0, 2), 6)

    def test_sum_range_list_single_element(self): self.assertEqual(sum_range_list([10, 20, 30], 1, 1), 20)

    def test_sum_range_list_from_zero(self): self.assertEqual(sum_range_list([5, 10, 15], 0, 1), 15)

    def test_sum_range_list_entire_list(self): self.assertEqual(sum_range_list([2, 4, 6, 8], 0, 3), 20)

