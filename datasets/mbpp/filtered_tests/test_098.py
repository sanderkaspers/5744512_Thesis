import unittest
from datasets.mbpp.programs.program_098 import *

class TestVersion(unittest.TestCase):
    def test_is_majority_with_1_2_3_3_3_3_10_7_3_expect_True(self):
        self.assertEqual(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3), True)

    def test_is_majority_with_1_1_2_4_4_4_6_6_8_4_expect_False(self):
        self.assertEqual(is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4), False)

    def test_is_majority_with_1_1_1_2_2_5_1_expect_True(self):
        self.assertEqual(is_majority([1, 1, 1, 2, 2], 5, 1), True)

