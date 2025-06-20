import unittest
from datasets.GPT_4.Few_shot1.programs.program_044 import *

class TestVersion(unittest.TestCase):
    def test_divisor_1(self): self.assertEqual(divisor(1), 1)

    def test_divisor_prime(self): self.assertEqual(divisor(7), 2)

    def test_divisor_even_composite(self): self.assertEqual(divisor(10), 4)

    def test_divisor_odd_composite(self): self.assertEqual(divisor(9), 3)

    def test_divisor_large_number(self): self.assertEqual(divisor(100), 9)

