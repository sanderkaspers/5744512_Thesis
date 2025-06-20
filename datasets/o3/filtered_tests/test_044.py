import unittest
from datasets.o3.programs.program_044 import *

class TestVersion(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(count_divisors(13), 2)

    def test_one(self):
        self.assertEqual(count_divisors(1), 1)

    def test_perfect_square(self):
        self.assertEqual(count_divisors(36), 9)

    def test_large_number(self):
        self.assertEqual(count_divisors(100), 9)

    def test_negative_input_raises(self):
        with self.assertRaises(ValueError):
            count_divisors(-4)

    def test_zero_input_raises(self):
        with self.assertRaises(ValueError):
            count_divisors(0)

