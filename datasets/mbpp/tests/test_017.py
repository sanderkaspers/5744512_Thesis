import unittest
from datasets.mbpp.programs.program_017 import *

class TestVersion(unittest.TestCase):
    def test_recursive_list_sum_with__1_2_3_4_5_6__expect_21(self):
        self.assertEqual(recursive_list_sum(([1, 2, [3,4],[5,6]])), 21)

    def test_recursive_list_sum_with__7_10_15_14_19_41__expect_106(self):
        self.assertEqual(recursive_list_sum(([7, 10, [15,14],[19,41]])), 106)

    def test_recursive_list_sum_with__10_20_30_40_50_60__expect_210(self):
        self.assertEqual(recursive_list_sum(([10, 20, [30,40],[50,60]])), 210)

