import unittest
from datasets.GPT_4.Zero_shot2.programs.program_069 import *

class TestVersion(unittest.TestCase):
    def test_mul_1(self):
        self.assertEqual(multiply_int(3, 4), 12)

    def test_mul_2(self):
        self.assertEqual(multiply_int(5, 0), 0)

    def test_mul_3(self):
        self.assertEqual(multiply_int(2, -3), -6)

    def test_mul_4(self):
        self.assertEqual(multiply_int(0, 10), 0)

    def test_mul_5(self):
        self.assertEqual(multiply_int(-2, -4), 8)

    def test_mul_6(self):
        self.assertEqual(multiply_int(-3, 3), -9)

    def test_mul_7(self):
        self.assertEqual(multiply_int(1, 100), 100)

