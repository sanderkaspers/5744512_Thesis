import unittest
from datasets.mbpp.programs.program_055 import *

class TestVersion(unittest.TestCase):
    def test_merge_sorted_list_with_25_24_15_4_5_29_110_19_20_11_56_25_233_154_24_26_54_(self):
        self.assertEqual(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]), [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233])

    def test_merge_sorted_list_with_1_3_5_6_8_9_2_5_7_11_1_4_7_8_12_expect__1(self):
        self.assertEqual(merge_sorted_list([1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]), [1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 11, 12])

    def test_merge_sorted_list_with_18_14_10_9_8_7_9_3_2_4_1_25_35_22_85_14_65_75_25_58_(self):
        self.assertEqual(merge_sorted_list([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1],[25, 35, 22, 85, 14, 65, 75, 25, 58],[12, 74, 9, 50, 61, 41]), [1, 2, 3, 4, 7, 8, 9, 9, 9, 10, 12, 14, 14, 18, 22, 25, 25, 35, 41, 50, 58, 61, 65, 74, 75, 85])

