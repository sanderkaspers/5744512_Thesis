import unittest
from datasets.mbpp.programs.program_046 import *

class TestVersion(unittest.TestCase):
    def test_multiply_num_with__8_2_3__1_7__expect__67_2(self):
        self.assertEqual(multiply_num((8, 2, 3, -1, 7)), -67.2)

    def test_multiply_num_with__10__20__30__expect__2000_0(self):
        self.assertEqual(multiply_num((-10,-20,-30)), -2000.0)

    def test_multiply_num_with__19_15_18__expect_1710_0(self):
        self.assertEqual(multiply_num((19,15,18)), 1710.0)

