import unittest
from datasets.mbpp.programs.program_021 import *

class TestVersion(unittest.TestCase):
    def test_is_sublist_with_2_4_3_5_7_3_7_expect_False(self):
        self.assertEqual(is_sublist([2,4,3,5,7],[3,7]), False)

    def test_is_sublist_with_2_4_3_5_7_4_3_expect_True(self):
        self.assertEqual(is_sublist([2,4,3,5,7],[4,3]), True)

    def test_is_sublist_with_2_4_3_5_7_1_6_expect_False(self):
        self.assertEqual(is_sublist([2,4,3,5,7],[1,6]), False)

