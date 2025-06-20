import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_065 import *

class TestVersion(unittest.TestCase):
    def test_limit_below_first_amicable(self): self.assertEqual(amicable_numbers_sum(100), 0)

    def test_limit_at_first_amicable_pair(self): self.assertEqual(amicable_numbers_sum(284), 504)

    def test_limit_above_two_amicable_pairs(self): self.assertEqual(amicable_numbers_sum(1300), 1714)

    def test_exact_known_sum_for_10000(self): self.assertEqual(amicable_numbers_sum(10000), 31626)

    def test_limit_is_one(self): self.assertEqual(amicable_numbers_sum(1), 0)

    def test_limit_is_not_integer_float(self): self.assertEqual(amicable_numbers_sum(100.5), 'Input is not an integer!')

    def test_limit_is_string(self): self.assertEqual(amicable_numbers_sum('500'), 'Input is not an integer!')

    def test_limit_is_zero(self): self.assertEqual(amicable_numbers_sum(0), 'Input must be bigger than 0!')

    def test_limit_is_negative(self): self.assertEqual(amicable_numbers_sum(-10), 'Input must be bigger than 0!')

    def test_partial_pair_under_limit(self): self.assertEqual(amicable_numbers_sum(220), 0)

