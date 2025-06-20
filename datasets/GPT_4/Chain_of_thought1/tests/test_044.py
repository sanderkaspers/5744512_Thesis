import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_044 import *

class TestVersion(unittest.TestCase):
    def test_common_divisor(self): self.assertEqual(divisor([4, 8, 12]), 4)

    def test_all_same(self): self.assertEqual(divisor([7, 7, 7]), 7)

    def test_pairwise_coprime(self): self.assertEqual(divisor([5, 9, 11]), 1)

    def test_gcd_is_element(self): self.assertEqual(divisor([6, 18, 24]), 6)

    def test_large_numbers(self): self.assertEqual(divisor([100000, 500000, 250000]), 50000)

    def test_two_elements(self): self.assertEqual(divisor([15, 20]), 5)

    def test_primes(self): self.assertEqual(divisor([13, 17, 19]), 1)

    def test_negative_numbers(self): self.assertEqual(divisor([-4, -8, -16]), 4)

    def test_contains_zero(self): self.assertEqual(divisor([0, 10, 20]), 10)

    def test_all_zeros(self): self.assertEqual(divisor([0, 0, 0]), 0)

    def test_single_element(self): self.assertEqual(divisor([42]), 42)

