import unittest
from datasets.GPT_4.Zero_shot1.programs.program_041 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(power(2, 3), 8)

    def test_2(self):
        self.assertEqual(power(5, 0), 1)

    def test_3(self):
        self.assertEqual(power(2, -2), 0.25)

    def test_4(self):
        self.assertEqual(power(0, 3), 0)

    def test_5(self):
        self.assertEqual(power(0, 0), 1)

    def test_6(self):
        self.assertEqual(power(-2, 3), -8)

    def test_7(self):
        self.assertEqual(power(-2, 2), 4)

    def test_8(self):
        self.assertEqual(power(-2, -3), -0.125)

    def test_9(self):
        self.assertAlmostEqual(power(2.5, 2), 6.25)

    def test_10(self):
        self.assertAlmostEqual(power(2.0, -2), 0.25)

    def test_11(self):
        self.assertEqual(power(2, 100), 1267650600228229401496703205376)

    def test_12(self):
        self.assertAlmostEqual(power(4, 0.5), 2.0)

    def test_13(self):
        self.assertAlmostEqual(power(9.0, 0.5), 3.0)

    def test_14(self):
        self.assertEqual(power(True, 3), 1)

