import unittest
from datasets.GPT_4.Zero_shot1.programs.program_075 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_negativenum([1, 2, 3]), 0)

    def test_2(self):
        self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_3(self):
        self.assertEqual(sum_negativenum([0, -1]), -1)

    def test_4(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_5(self):
        self.assertEqual(sum_negativenum([-99]), -99)

    def test_6(self):
        self.assertEqual(sum_negativenum([1.5, -2.5, -3.0]), -5.5)

    def test_7(self):
        self.assertEqual(sum_negativenum([0]), 0)

    def test_8(self):
        self.assertIsInstance(sum_negativenum([-1, -2]), (int, float))

