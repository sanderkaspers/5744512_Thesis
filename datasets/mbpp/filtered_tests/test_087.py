import unittest
from datasets.mbpp.programs.program_087 import *

class TestVersion(unittest.TestCase):
    def test_sum_series_with_6_expect_12(self):
        self.assertEqual(sum_series(6), 12)

    def test_sum_series_with_10_expect_30(self):
        self.assertEqual(sum_series(10), 30)

    def test_sum_series_with_9_expect_25(self):
        self.assertEqual(sum_series(9), 25)

