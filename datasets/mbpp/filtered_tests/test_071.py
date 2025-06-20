import unittest
from datasets.mbpp.programs.program_071 import *

class TestVersion(unittest.TestCase):
    def test_magic_square_test_with_7_12_1_14_2_13_8_11_16_3_10_5_9_6_15_4_expect_True(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

    def test_magic_square_test_with_2_7_6_9_5_1_4_3_8_expect_True(self):
        self.assertEqual(magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]]), True)

    def test_magic_square_test_with_2_7_6_9_5_1_4_3_7_expect_False(self):
        self.assertEqual(magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]]), False)

