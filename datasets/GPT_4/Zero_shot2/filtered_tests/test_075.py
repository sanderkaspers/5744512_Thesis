import unittest
from datasets.GPT_4.Zero_shot2.programs.program_075 import *

class TestVersion(unittest.TestCase):
    def test_neg_1(self):
        self.assertEqual(sum_negativenum([1, -2, 3, -4]), -6)

    def test_neg_2(self):
        self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_neg_3(self):
        self.assertEqual(sum_negativenum([1, 2, 3]), 0)

    def test_neg_4(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_neg_5(self):
        self.assertEqual(sum_negativenum([0]), 0)

    def test_neg_6(self):
        self.assertEqual(sum_negativenum([-7]), -7)

    def test_neg_7(self):
        self.assertEqual(sum_negativenum([8]), 0)

    def test_neg_8(self):
        self.assertEqual(sum_negativenum([-1]*1000), -1000)

