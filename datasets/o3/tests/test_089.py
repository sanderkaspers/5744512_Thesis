import unittest
from datasets.o3.programs.program_089 import *

class TestVersion(unittest.TestCase):
    def test_perfect_number(self):
        self.assertEqual(div_sum(6), 6)

    def test_prime_number(self):
        self.assertEqual(div_sum(7), 1)

    def test_square_number(self):
        self.assertEqual(div_sum(25), 6)

    def test_one(self):
        self.assertEqual(div_sum(1), 1)

    def test_large_composite(self):
        self.assertEqual(div_sum(100), 117)

    def test_zero(self):
        self.assertEqual(div_sum(0), 1)

