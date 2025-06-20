import unittest
from datasets.mbpp.programs.program_041 import *

class TestVersion(unittest.TestCase):
    def test_power_with_3_4_expect_81(self):
        self.assertEqual(power(3,4), 81)

    def test_power_with_2_3_expect_8(self):
        self.assertEqual(power(2,3), 8)

    def test_power_with_5_5_expect_3125(self):
        self.assertEqual(power(5,5), 3125)

