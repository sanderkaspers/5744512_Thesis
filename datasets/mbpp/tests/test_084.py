import unittest
from datasets.mbpp.programs.program_084 import *

class TestVersion(unittest.TestCase):
    def test_max_Abs_Diff_with__2_1_5_3__expect_4(self):
        self.assertEqual(max_Abs_Diff((2,1,5,3)), 4)

    def test_max_Abs_Diff_with__9_3_2_5_1__expect_8(self):
        self.assertEqual(max_Abs_Diff((9,3,2,5,1)), 8)

    def test_max_Abs_Diff_with__3_2_1__expect_2(self):
        self.assertEqual(max_Abs_Diff((3,2,1)), 2)

