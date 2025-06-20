import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_068 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum(12, 18), 6)  # Common divisors: 1, 2, 3, 6

    def test_prime_numbers(self):
        self.assertEqual(sum(13, 17), 1)  # Common divisor: 1

    def test_multiple_case(self):
        self.assertEqual(sum(10, 5), 3)  # Common divisors: 1, 5

    def test_same_numbers(self):
        self.assertEqual(sum(15, 15), 9)  # Common divisors: 1, 3, 5, 15

    def test_no_common_divisors(self):
        self.assertEqual(sum(8, 9), 1)  # Common divisor: 1

    def test_one_number_is_one(self):
        self.assertEqual(sum(1, 10), 1)  # Common divisor: 1

    def test_both_numbers_are_one(self):
        self.assertEqual(sum(1, 1), 1)  # Common divisor: 1

    def test_very_large_numbers(self):
        self.assertEqual(sum(1000000, 500000), 500001)  # Common divisors include 1, 2, 4, ... up to 500000

    def test_negative_numbers(self):
        self.assertEqual(sum(-12, -18), 6)  # Common divisors: 1, 2, 3, 6 (ignoring negative sign)

    def test_zero_as_number(self):
        self.assertEqual(sum(0, 5), 0)  # No common divisors with 0

