import unittest
from datasets.GPT_4.Zero_shot1.programs.program_046 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(multiply_num([1, 2, 3]), 6)

    def test_2(self):
        self.assertEqual(multiply_num([1, 0, 3]), 0)

    def test_3(self):
        self.assertEqual(multiply_num([-1, -2, -3]), -6)

    def test_4(self):
        self.assertEqual(multiply_num([-2, 3]), -6)

    def test_5(self):
        self.assertEqual(multiply_num([5]), 5)

    def test_6(self):
        self.assertEqual(multiply_num([]), 1)

    def test_7(self):
        self.assertEqual(multiply_num([1, 1, 1]), 1)

    def test_8(self):
        self.assertEqual(multiply_num([0, 0, 0]), 0)

    def test_9(self):
        self.assertAlmostEqual(multiply_num([1.5, 2]), 3.0)

    def test_10(self):
        self.assertAlmostEqual(multiply_num([2, 0.5]), 1.0)

    def test_11(self):
        self.assertEqual(multiply_num([10000, 10000]), 100000000)

    def test_12(self):
        self.assertEqual(multiply_num([True, 2, 3]), 6)

    def test_13(self):
        self.assertEqual(multiply_num([0]), 0)

    def test_14(self):
        self.assertEqual(multiply_num([1]*1000), 1)

    def test_15(self):
        self.assertEqual(multiply_num([-2, -2]), 4)

    def test_16(self):
        self.assertEqual(multiply_num([-2, -2, -2]), -8)

