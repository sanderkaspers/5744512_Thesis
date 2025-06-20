import unittest
from datasets.mbpp.programs.program_003 import *

class TestVersion(unittest.TestCase):
    def test_find_Volume_with_10_8_6_expect_240(self):
        self.assertEqual(find_Volume(10,8,6), 240)

    def test_find_Volume_with_3_2_2_expect_6(self):
        self.assertEqual(find_Volume(3,2,2), 6)

    def test_find_Volume_with_1_2_1_expect_1(self):
        self.assertEqual(find_Volume(1,2,1), 1)

