import unittest
from datasets.GPT_4.Few_shot1.programs.program_089 import *

class TestVersion(unittest.TestCase):
    def test_are_equivalent_perfect_numbers(self): self.assertTrue(are_equivalent(6, 28))

    def test_are_equivalent_equal_inputs(self): self.assertTrue(are_equivalent(12, 12))

    def test_are_equivalent_prime_numbers(self): self.assertTrue(are_equivalent(2, 3))

    def test_are_equivalent_prime_and_composite(self): self.assertFalse(are_equivalent(2, 4))

    def test_are_equivalent_zero_input(self): self.assertTrue(are_equivalent(0, 0))

    def test_are_equivalent_one_input(self): self.assertTrue(are_equivalent(1, 1))

    def test_are_equivalent_one_and_other(self): self.assertFalse(are_equivalent(1, 2))

    def test_are_equivalent_composites_same_sum(self): self.assertTrue(are_equivalent(6, 10))

    def test_are_equivalent_composites_different_sum(self): self.assertFalse(are_equivalent(6, 9))

    def test_are_equivalent_large_numbers(self): self.assertTrue(are_equivalent(496, 28))

    def test_are_equivalent_one_zero(self): self.assertFalse(are_equivalent(0, 1))

    def test_are_equivalent_with_non_divisor_sum_match(self): self.assertFalse(are_equivalent(14, 15))

    def test_are_equivalent_large_different(self): self.assertFalse(are_equivalent(1000, 500))

    def test_are_equivalent_perfect_and_non_perfect(self): self.assertFalse(are_equivalent(28, 27))

    def test_are_equivalent_same_divisor_sum_different_numbers(self): self.assertTrue(are_equivalent(14, 20))

