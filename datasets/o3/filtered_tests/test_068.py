import unittest
from datasets.o3.programs.program_068 import *

class TestVersion(unittest.TestCase):
    def test_common_divisors(self):
        self.assertEqual(sum(12,18), 12)

    def test_no_common_divisors_except_one(self):
        self.assertEqual(sum(8,9), 1)

    def test_same_numbers(self):
        self.assertEqual(sum(4,4), 3)

    def test_with_one(self):
        self.assertEqual(sum(1,10), 0)

    def test_prime_numbers(self):
        self.assertEqual(sum(5,7), 1)

