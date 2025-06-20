import unittest
from datasets.GPT_4.Few_shot2.programs.program_068 import *

class TestVersion(unittest.TestCase):
    def test_sum_positive_range(self): self.assertEqual(sum(1, 5), 15)

    def test_sum_single_element(self): self.assertEqual(sum(4, 4), 4)

    def test_sum_zero_to_positive(self): self.assertEqual(sum(0, 3), 6)

    def test_sum_negative_to_positive(self): self.assertEqual(sum(-2, 2), 0)

    def test_sum_negative_range(self): self.assertEqual(sum(-4, -1), -10)

    def test_sum_zero_range(self): self.assertEqual(sum(0, 0), 0)

    def test_sum_larger_to_smaller(self): self.assertEqual(sum(5, 1), 0)

    def test_sum_reverse_range_should_sum_negative(self): self.assertEqual(sum(3, 1), 0)

    def test_sum_large_range(self): self.assertEqual(sum(1, 100), 5050)

