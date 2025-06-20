import unittest
from datasets.GPT_4.Zero_shot2.programs.program_092 import *

class TestVersion(unittest.TestCase):
    def test_power_1(self):
        self.assertEqual(next_power_of_2(4), 4)

    def test_power_2(self):
        self.assertEqual(next_power_of_2(7), 8)

    def test_power_3(self):
        self.assertEqual(next_power_of_2(9), 16)

    def test_power_4(self):
        self.assertEqual(next_power_of_2(0), 1)

    def test_power_5(self):
        self.assertEqual(next_power_of_2(1), 1)

    def test_power_6(self):
        self.assertEqual(next_power_of_2(2), 2)

    def test_power_7(self):
        self.assertEqual(next_power_of_2(255), 256)

    def test_power_8(self):
        self.fail("Negative input not supported by implementation; test would hang.") # self.assertEqual(next_power_of_2(-5), 1)

