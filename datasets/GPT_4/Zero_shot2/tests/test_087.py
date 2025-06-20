import unittest
from datasets.GPT_4.Zero_shot2.programs.program_087 import *

class TestVersion(unittest.TestCase):
    def test_series_1(self):
        self.assertEqual(sum_series(5), 9)

    def test_series_2(self):
        self.assertEqual(sum_series(6), 12)

    def test_series_3(self):
        self.assertEqual(sum_series(0), 0)

    def test_series_4(self):
        self.assertEqual(sum_series(-1), 0)

    def test_series_5(self):
        self.assertEqual(sum_series(1), 1)

    def test_series_6(self):
        self.assertEqual(sum_series(10), 30)

    def test_series_7(self):
        self.assertEqual(sum_series(100), 2550)

