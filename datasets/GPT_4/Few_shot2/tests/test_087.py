import unittest
from datasets.GPT_4.Few_shot2.programs.program_087 import *

class TestVersion(unittest.TestCase):
    def test_sum_series_basic(self): self.assertEqual(sum_series(5), 15)

    def test_sum_series_zero(self): self.assertEqual(sum_series(0), 0)

    def test_sum_series_negative(self): self.assertEqual(sum_series(-3), 0)

    def test_sum_series_one(self): self.assertEqual(sum_series(1), 1)

    def test_sum_series_two(self): self.assertEqual(sum_series(2), 3)

    def test_sum_series_large(self): self.assertEqual(sum_series(10), 55)

