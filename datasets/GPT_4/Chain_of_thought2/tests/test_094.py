import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_094 import *

class TestVersion(unittest.TestCase):
    def test_basic_range(self): self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 9)

    def test_single_index(self): self.assertEqual(sum_range_list([10, 20, 30], 1, 1), 20)

    def test_full_range(self): self.assertEqual(sum_range_list([1, 2, 3, 4], 0, 3), 10)

    def test_negative_numbers(self): self.assertEqual(sum_range_list([5, -2, -3, 4], 1, 2), -5)

    def test_zeros_in_list(self): self.assertEqual(sum_range_list([0, 0, 5, 0], 0, 3), 5)

    def test_m_greater_than_n(self): self.assertEqual(sum_range_list([1, 2, 3], 2, 1), 0)

    def test_negative_index(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4], -2, 2), 9)

    def test_large_list(self): self.assertEqual(sum_range_list(list(range(100)), 10, 19), sum(range(10, 20)))

