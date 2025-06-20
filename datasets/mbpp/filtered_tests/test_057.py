import unittest
from datasets.mbpp.programs.program_057 import *

class TestVersion(unittest.TestCase):
    def test_common_in_nested_lists_with_12_18_23_25_45_7_12_18_24_28_1_5_8_12_15_16_18_(self):
        self.assertCountEqual(
        common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]),
        [12, 18]
        )

    def test_common_in_nested_lists_with_12_5_23_25_45_7_11_5_23_28_1_5_8_18_23_16_expec(self):
        self.assertCountEqual(
        common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]),
        [5, 23]
        )

    def test_common_in_nested_lists_with_2_3_4_1_4_5_6_4_8_4_5_6_8_4_expect__4(self):
        self.assertEqual(common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]]), [4])

