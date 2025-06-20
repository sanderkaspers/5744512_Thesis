import unittest
from datasets.mbpp.programs.program_092 import *

class TestVersion(unittest.TestCase):
    def test_next_power_of_2_with_0_expect_1(self):
        self.assertEqual(next_power_of_2(0), 1)

    def test_next_power_of_2_with_5_expect_8(self):
        self.assertEqual(next_power_of_2(5), 8)

    def test_next_power_of_2_with_17_expect_32(self):
        self.assertEqual(next_power_of_2(17), 32)

