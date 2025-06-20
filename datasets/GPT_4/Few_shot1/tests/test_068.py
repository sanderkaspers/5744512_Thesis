import unittest
from datasets.GPT_4.Few_shot1.programs.program_068 import *

class TestVersion(unittest.TestCase):
    def test_sum_common_divisors_basic(self): self.assertEqual(sum(10, 15), 6)

    def test_sum_common_divisors_primes(self): self.assertEqual(sum(7, 13), 1)

    def test_sum_common_divisors_one_value_is_one(self): self.assertEqual(sum(1, 10), 1)

    def test_sum_common_divisors_same_values(self): self.assertEqual(sum(12, 12), 16)

    def test_sum_common_divisors_no_common_except_one(self): self.assertEqual(sum(9, 16), 1)

    def test_sum_common_divisors_large_values(self): self.assertEqual(sum(100, 80), 42)

    def test_sum_common_divisors_a_less_than_b(self): self.assertEqual(sum(6, 18), 6)

    def test_sum_common_divisors_b_less_than_a(self): self.assertEqual(sum(18, 6), 6)

    def test_sum_common_divisors_min_equal_one(self): self.assertEqual(sum(1, 1), 0)

    def test_sum_common_divisors_including_zero(self): self.assertEqual(sum(0, 10), 0)

