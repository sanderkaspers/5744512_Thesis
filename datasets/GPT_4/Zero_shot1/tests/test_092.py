import unittest
from datasets.GPT_4.Zero_shot1.programs.program_092 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(next_power_of_2(1), 1)

    def test_2(self):
        self.assertEqual(next_power_of_2(2), 2)

    def test_3(self):
        self.assertEqual(next_power_of_2(3), 4)

    def test_4(self):
        self.assertEqual(next_power_of_2(5), 8)

    def test_5(self):
        self.assertEqual(next_power_of_2(9), 16)

    def test_6(self):
        self.assertEqual(next_power_of_2(1024), 1024)

    def test_7(self):
        self.assertEqual(next_power_of_2(1025), 2048)

    def test_8(self):
        self.fail("Negative input not supported by implementation; test would hang.") # self.assertEqual(next_power_of_2(-7), 1)

    def test_9(self):
        self.assertIsInstance(next_power_of_2(2047), int)

