import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_087 import *

class TestVersion(unittest.TestCase):
    def test_odd_input(self): self.assertEqual(sum_series(5), 9)

    def test_even_input(self): self.assertEqual(sum_series(6), 12)

    def test_one(self): self.assertEqual(sum_series(1), 1)

    def test_zero(self): self.assertEqual(sum_series(0), 0)

    def test_negative_one(self): self.assertEqual(sum_series(-1), 0)

    def test_large_even(self): self.assertEqual(sum_series(10), 30)

    def test_large_odd(self): self.assertEqual(sum_series(9), 25)

    def test_negative_even(self): self.assertEqual(sum_series(-4), 0)

    def test_boolean_input(self): self.assertEqual(sum_series(True), 1)

