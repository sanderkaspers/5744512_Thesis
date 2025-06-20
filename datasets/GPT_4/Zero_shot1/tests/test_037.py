import unittest
from datasets.GPT_4.Zero_shot1.programs.program_037 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(closest_num(0), -1)

    def test_2(self):
        self.assertEqual(closest_num(-1), -2)

    def test_3(self):
        self.assertEqual(closest_num(1000000), 999999)

    def test_4(self):
        self.assertEqual(closest_num(-1000000), -1000001)

    def test_5(self):
        self.assertEqual(closest_num(1.5), 0.5)

    def test_6(self):
        self.assertEqual(closest_num(2.0), 1.0)

    def test_7(self):
        self.assertEqual(closest_num(True), 0)

    def test_8(self):
        self.assertEqual(closest_num(False), -1)

    def test_9(self):
        import math
        self.assertEqual(closest_num(math.inf), math.inf)

