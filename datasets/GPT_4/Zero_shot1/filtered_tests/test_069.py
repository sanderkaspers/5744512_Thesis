import unittest
from datasets.GPT_4.Zero_shot1.programs.program_069 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(multiply_int(3, 4), 12)

    def test_2(self):
        self.assertEqual(multiply_int(5, 0), 0)

    def test_3(self):
        self.assertEqual(multiply_int(-3, 4), -12)

    def test_4(self):
        self.assertEqual(multiply_int(3, -4), -12)

    def test_5(self):
        self.assertEqual(multiply_int(-3, -4), 12)

    def test_6(self):
        self.assertEqual(multiply_int(0, 7), 0)

    def test_7(self):
        self.assertEqual(multiply_int(0, 0), 0)

    def test_8(self):
        self.assertEqual(multiply_int(1, 100), 100)

