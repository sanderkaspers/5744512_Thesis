import unittest
from datasets.GPT_4.Zero_shot2.programs.program_046 import *

class TestVersion(unittest.TestCase):
    def test_mul_1(self):
        self.assertEqual(multiply_num([2, 3, 4]), 24)

    def test_mul_2(self):
        self.assertEqual(multiply_num([2, 0, 4]), 0)

    def test_mul_3(self):
        self.assertEqual(multiply_num([0, 0, 0]), 0)

    def test_mul_4(self):
        self.assertEqual(multiply_num([2, -3]), -6)

    def test_mul_5(self):
        self.assertEqual(multiply_num([-2, -3]), 6)

    def test_mul_6(self):
        self.assertEqual(multiply_num([1, -1, 0, 2]), 0)

    def test_mul_7(self):
        self.assertEqual(multiply_num([5]), 5)

    def test_mul_8(self):
        self.assertEqual(multiply_num([]), 1)

    def test_mul_9(self):
        self.assertAlmostEqual(multiply_num([1.5, 2]), 3.0)

    def test_mul_10(self):
        self.assertEqual(multiply_num([1]*100), 1)

    def test_mul_11(self):
        self.assertEqual(multiply_num([1, 2, 3]), 6)

    def test_mul_12(self):
        self.assertEqual(multiply_num([1, 1, 1]), 1)

    def test_mul_13(self):
        self.assertEqual(multiply_num([-1, -1]), 1)

    def test_mul_14(self):
        self.assertAlmostEqual(multiply_num([0.5, 0.2]), 0.1)

    def test_mul_15(self):
        self.assertEqual(multiply_num([True, False, 5]), 0)

    def test_mul_16(self):
        self.assertEqual(multiply_num([2, 2, 2]), 8)

    def test_mul_17(self):
        self.assertAlmostEqual(multiply_num([2, 2.5]), 5.0)

    def test_mul_18(self):
        self.assertEqual(multiply_num([100000, 100000]), 10000000000)

    def test_mul_19(self):
        self.assertAlmostEqual(multiply_num([0.1, 0.01, 0.001]), 0.000001)

