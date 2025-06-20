import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_068 import *

class TestVersion(unittest.TestCase):
    def test_coprime_numbers(self): self.assertEqual(sum(8, 15), 1)

    def test_same_numbers(self): self.assertEqual(sum(6, 6), 12)

    def test_one_multiple_of_other(self): self.assertEqual(sum(10, 5), 6)

    def test_both_even(self): self.assertEqual(sum(12, 18), 12)

    def test_prime_and_composite(self): self.assertEqual(sum(13, 26), 14)

    def test_one_input_is_one(self): self.assertEqual(sum(1, 9), 1)

    def test_equal_primes(self): self.assertEqual(sum(7, 7), 8)

    def test_zero_input(self): self.assertEqual(sum(0, 10), 0)

    def test_both_zeros(self): self.assertEqual(sum(0, 0), 0)

    def test_negative_inputs(self): self.assertEqual(sum(-6, -9), 4)

    def test_negative_and_positive(self): self.assertEqual(sum(-12, 18), 12)

