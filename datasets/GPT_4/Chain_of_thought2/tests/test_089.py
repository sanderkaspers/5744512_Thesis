import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_089 import *

class TestVersion(unittest.TestCase):
    def test_equal_sum_of_divisors(self): self.assertTrue(are_equivalent(6, 6))

    def test_different_sum_of_divisors(self): self.assertFalse(are_equivalent(6, 8))

    def test_two_perfect_numbers(self): self.assertFalse(are_equivalent(6, 28))

    def test_same_divisor_sum_different_numbers(self): self.assertTrue(are_equivalent(220, 284))

    def test_both_primes(self): self.assertTrue(are_equivalent(7, 13))

    def test_prime_and_composite(self): self.assertFalse(are_equivalent(5, 6))

    def test_with_one_as_input(self): self.assertTrue(are_equivalent(1, 1))

    def test_zero_and_number(self): self.assertFalse(are_equivalent(0, 1))

    def test_large_numbers(self): self.assertFalse(are_equivalent(1000, 496))

    def test_negative_inputs(self): self.assertTrue(are_equivalent(-6, -6))

