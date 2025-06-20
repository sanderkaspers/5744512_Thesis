import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_089 import *

class TestVersion(unittest.TestCase):
    def test_perfect_numbers(self): self.assertTrue(are_equivalent(6, 28))

    def test_different_sums(self): self.assertFalse(are_equivalent(10, 14))

    def test_similar_not_equal(self): self.assertFalse(are_equivalent(12, 16))

    def test_same_number(self): self.assertTrue(are_equivalent(15, 15))

    def test_both_ones(self): self.assertTrue(are_equivalent(1, 1))

    def test_prime_numbers(self): self.assertTrue(are_equivalent(2, 3))

    def test_zero_input(self): self.assertFalse(are_equivalent(0, 6))

    def test_negative_input(self): self.assertFalse(are_equivalent(-6, 6))

    def test_large_input(self): result = are_equivalent(1000000, 999983); self.assertIsInstance(result, bool)

