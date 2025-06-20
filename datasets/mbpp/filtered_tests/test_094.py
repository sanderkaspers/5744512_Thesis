import unittest
from datasets.mbpp.programs.program_094 import *

class TestVersion(unittest.TestCase):
    def test_sum_range_list_with_2_1_5_6_8_3_4_9_10_11_8_12_8_10_expect_29(self):
        self.assertEqual(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12],8,10), 29)

    def test_sum_range_list_with_2_1_5_6_8_3_4_9_10_11_8_12_5_7_expect_16(self):
        self.assertEqual(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12],5,7), 16)

    def test_sum_range_list_with_2_1_5_6_8_3_4_9_10_11_8_12_7_10_expect_38(self):
        self.assertEqual(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12],7,10), 38)

