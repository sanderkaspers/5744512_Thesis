import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_089 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(are_equivalent(6, 28))

    def test_different_sums(self):
        self.assertFalse(are_equivalent(6, 12))

    def test_prime_numbers(self):
        self.assertFalse(are_equivalent(7, 11))

    def test_one_as_input(self):
        self.assertFalse(are_equivalent(1, 6))

    def test_same_numbers(self):
        self.assertTrue(are_equivalent(12, 12))

    def test_zero_as_input(self):
        self.assertFalse(are_equivalent(0, 6))

    def test_negative_numbers(self):
        self.assertFalse(are_equivalent(-6, 6))

    def test_small_composite_numbers(self):
        self.assertFalse(are_equivalent(4, 6))

    def test_large_numbers(self):
        self.assertFalse(are_equivalent(1000000, 999999))

    def test_perfect_numbers(self):
        self.assertTrue(are_equivalent(28, 28))

