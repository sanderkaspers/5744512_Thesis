import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_087 import *

class TestVersion(unittest.TestCase):
    def test_odd_n(self): self.assertEqual(sum_series(5), 9)

    def test_even_n(self): self.assertEqual(sum_series(6), 12)

    def test_n_is_one(self): self.assertEqual(sum_series(1), 1)

    def test_n_is_two(self): self.assertEqual(sum_series(2), 2)

    def test_n_is_zero(self): self.assertEqual(sum_series(0), 0)

    def test_negative_n(self): self.assertEqual(sum_series(-5), 0)

    def test_large_n(self): self.assertEqual(sum_series(100), 2550)

