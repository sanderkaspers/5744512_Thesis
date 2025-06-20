import unittest
from datasets.GPT_4.Zero_shot2.programs.program_041 import *

class TestVersion(unittest.TestCase):
    def test_pow_1(self):
        self.assertEqual(power(2, 0), 1)

    def test_pow_2(self):
        self.assertEqual(power(2, 3), 8)

    def test_pow_3(self):
        self.assertEqual(power(-2, 2), 4)

    def test_pow_4(self):
        self.assertEqual(power(-2, 3), -8)

    def test_pow_5(self):
        self.assertEqual(power(0, 2), 0)

    def test_pow_6(self):
        self.assertEqual(power(0, 0), 1)

    def test_pow_7(self):
        self.assertEqual(power(3, 1), 3)

    def test_pow_8(self):
        self.assertAlmostEqual(power(1.5, 2), 2.25)

    def test_pow_9(self):
        self.assertEqual(power(2, 10), 1024)

    def test_pow_10(self):
        self.assertEqual(power(1, 100), 1)

    def test_pow_11(self):
        self.assertEqual(power(-1, 4), 1)
        self.assertEqual(power(-1, 3), -1)

    def test_pow_12(self):
        self.assertEqual(power(2, 10), 1024)

    def test_pow_13(self):
        self.assertEqual(power(5, 3), 125)

    def test_pow_14(self):
        self.assertEqual(power(10, 0), 1)

    def test_pow_15(self):
        self.assertEqual(power(0, 1), 0)

    def test_pow_16(self):
        self.assertEqual(power(-10, 2), 100)

    def test_pow_17(self):
        self.assertAlmostEqual(power(2.0, 3), 8.0)

