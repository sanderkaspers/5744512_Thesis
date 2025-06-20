import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_044 import *

class TestVersion(unittest.TestCase):
    def test_prime_number(self): self.assertEqual(divisor(7), 2)

    def test_perfect_square(self): self.assertEqual(divisor(9), 3)

    def test_highly_composite(self): self.assertEqual(divisor(12), 6)

    def test_one(self): self.assertEqual(divisor(1), 1)

    def test_two(self): self.assertEqual(divisor(2), 2)

    def test_negative_input(self): self.assertEqual(divisor(-6), 4)

    def test_large_input(self): self.assertEqual(divisor(100), 9)

