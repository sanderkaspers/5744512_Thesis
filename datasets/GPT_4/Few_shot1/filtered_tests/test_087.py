import unittest
from datasets.GPT_4.Few_shot1.programs.program_087 import *

class TestVersion(unittest.TestCase):
    def test_sum_series_zero(self): self.assertEqual(sum_series(0), 0)

    def test_sum_series_negative(self): self.assertEqual(sum_series(-5), 0)

    def test_sum_series_one(self): self.assertEqual(sum_series(1), 1)

    def test_sum_series_two(self): self.assertEqual(sum_series(2), 2)

    def test_sum_series_three(self): self.assertEqual(sum_series(3), 4)

    def test_sum_series_four(self): self.assertEqual(sum_series(4), 6)

    def test_sum_series_five(self): self.assertEqual(sum_series(5), 9)

    def test_sum_series_six(self): self.assertEqual(sum_series(6), 12)

    def test_sum_series_seven(self): self.assertEqual(sum_series(7), 16)

    def test_sum_series_eight(self): self.assertEqual(sum_series(8), 20)

    def test_sum_series_nine(self): self.assertEqual(sum_series(9), 25)

    def test_sum_series_ten(self): self.assertEqual(sum_series(10), 30)

    def test_sum_series_large_odd(self): self.assertEqual(sum_series(101), sum(range(1, 102, 2)))

    def test_sum_series_large_even(self): self.assertEqual(sum_series(100), sum(range(0, 101, 2)))

