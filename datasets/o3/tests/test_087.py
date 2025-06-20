import unittest
from datasets.o3.programs.program_087 import *

class TestVersion(unittest.TestCase):
    def test_sum_series_one(self):
        self.assertEqual(sum_series(1), 1)

    def test_sum_series_five(self):
        self.assertEqual(sum_series(5), 15)

    def test_sum_series_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_sum_series_negative(self):
        self.assertEqual(sum_series(-4), 0)

    def test_sum_series_large(self):
        self.assertEqual(sum_series(100), 5050)

    def test_sum_series_float(self):
        self.assertEqual(sum_series(5.0), 15.0)

