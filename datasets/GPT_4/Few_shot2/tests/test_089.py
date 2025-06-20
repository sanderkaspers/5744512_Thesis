import unittest
from datasets.GPT_4.Few_shot2.programs.program_089 import *

class TestVersion(unittest.TestCase):
    def test_div_sum_perfect_number(self): self.assertEqual(div_sum(28), 28)

    def test_div_sum_prime_number(self): self.assertEqual(div_sum(13), 1)

    def test_div_sum_composite_number(self): self.assertEqual(div_sum(12), 16)

    def test_div_sum_one(self): self.assertEqual(div_sum(1), 1)

    def test_div_sum_two(self): self.assertEqual(div_sum(2), 1)

    def test_div_sum_square_number(self): self.assertEqual(div_sum(36), 55)

    def test_div_sum_large_number(self): self.assertEqual(div_sum(100), 117)

    def test_div_sum_even_number(self): self.assertEqual(div_sum(18), 21)

    def test_div_sum_odd_number(self): self.assertEqual(div_sum(15), 9)

