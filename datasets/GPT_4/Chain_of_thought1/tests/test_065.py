import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_065 import *

class TestVersion(unittest.TestCase):
    def test_limit_300(self): self.assertEqual(amicable_numbers_sum(300), 504)

    def test_limit_1000(self): self.assertEqual(amicable_numbers_sum(1000), 504)

    def test_limit_one(self): self.assertEqual(amicable_numbers_sum(1), 0)

    def test_limit_10000(self): self.assertEqual(amicable_numbers_sum(10000), 31626)

    def test_small_prime_limit(self): self.assertEqual(amicable_numbers_sum(3), 0)

    def test_zero_limit(self): self.assertEqual(amicable_numbers_sum(0), 0)

    def test_negative_limit(self): self.assertEqual(amicable_numbers_sum(-50), 0)

    def test_float_limit(self): self.assertEqual(amicable_numbers_sum(999.99), 0)

    def test_string_limit(self): self.assertEqual(amicable_numbers_sum('1000'), 0)

    def test_limit_10000(self): self.assertEqual(amicable_numbers_sum(10000), 83760)

