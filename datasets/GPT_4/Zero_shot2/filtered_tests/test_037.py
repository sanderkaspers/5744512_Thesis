import unittest
from datasets.GPT_4.Zero_shot2.programs.program_037 import *

class TestVersion(unittest.TestCase):
    def test_close_1(self):
        self.assertEqual(closest_num(10), 9)

    def test_close_2(self):
        self.assertEqual(closest_num(0), -1)

    def test_close_3(self):
        self.assertEqual(closest_num(-5), -6)

    def test_close_4(self):
        self.assertEqual(closest_num(1000000), 999999)

    def test_close_5(self):
        self.assertEqual(closest_num(1), 0)

    def test_close_6(self):
        self.assertEqual(closest_num(3.5), 2.5)

    def test_close_7(self):
        self.assertEqual(closest_num(True), 0)

    def test_close_8(self):
        self.assertEqual(closest_num(False), -1)

