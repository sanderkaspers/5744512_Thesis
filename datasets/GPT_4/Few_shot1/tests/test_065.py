import unittest
from datasets.GPT_4.Few_shot1.programs.program_065 import *

class TestVersion(unittest.TestCase):
    def test_amicable_basic(self): self.assertEqual(amicable_numbers_sum(300), 504)

    def test_amicable_limit_exact(self): self.assertEqual(amicable_numbers_sum(220), 504)

    def test_amicable_zero(self): self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")

    def test_amicable_negative(self): self.assertEqual(amicable_numbers_sum(-10), "Input must be bigger than 0!")

    def test_amicable_non_integer_string(self): self.assertEqual(amicable_numbers_sum("100"), "Input is not an integer!")

    def test_amicable_non_integer_float(self): self.assertEqual(amicable_numbers_sum(100.5), "Input is not an integer!")

    def test_amicable_one(self): self.assertEqual(amicable_numbers_sum(1), 0)

    def test_amicable_two(self): self.assertEqual(amicable_numbers_sum(2), 0)

    def test_amicable_large_limit(self): self.assertEqual(amicable_numbers_sum(10000), 31626)

    def test_amicable_no_pairs(self): self.assertEqual(amicable_numbers_sum(200), 0)

