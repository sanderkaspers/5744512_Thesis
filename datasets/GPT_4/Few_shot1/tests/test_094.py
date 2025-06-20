import unittest
from datasets.GPT_4.Few_shot1.programs.program_094 import *

class TestVersion(unittest.TestCase):
    def test_sum_range_full(self): self.assertEqual(sum_range_list([1, 2, 3, 4], 0, 3), 10)

    def test_sum_range_partial(self): self.assertEqual(sum_range_list([5, 10, 15, 20], 1, 2), 25)

    def test_sum_range_single_element(self): self.assertEqual(sum_range_list([7, 8, 9], 1, 1), 8)

    def test_sum_range_start_zero(self): self.assertEqual(sum_range_list([1, 2, 3], 0, 1), 3)

    def test_sum_range_last_element(self): self.assertEqual(sum_range_list([10, 20, 30], 2, 2), 30)

    def test_sum_range_entire_list(self): self.assertEqual(sum_range_list([1, 1, 1, 1], 0, 3), 4)

    def test_sum_range_negative_index(self): self.assertEqual(sum_range_list([10, 20, 30], -1, 1), 50)

    def test_sum_range_negative_range(self): self.assertEqual(sum_range_list([10, 20, 30, 40], -2, -1), 50)

    def test_sum_range_large_list(self): self.assertEqual(sum_range_list(list(range(100)), 10, 20), sum(range(10, 21)))

    def test_sum_range_m_equals_n_at_end(self): self.assertEqual(sum_range_list([3, 6, 9, 12], 3, 3), 12)

    def test_sum_range_single_item_list(self): self.assertEqual(sum_range_list([5], 0, 0), 5)

    def test_sum_range_floats(self): self.assertEqual(sum_range_list([1.1, 2.2, 3.3], 0, 2), 6.6)

