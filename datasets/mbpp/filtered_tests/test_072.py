import unittest
from datasets.mbpp.programs.program_072 import *

class TestVersion(unittest.TestCase):
    def test_max_occurrences_with_2_3_8_4_7_9_8_2_6_5_1_6_1_2_3_2_4_6_9_1_2_expect__2(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), (2))

    def test_max_occurrences_with_2_3_8_4_7_9_8_7_9_15_14_10_12_13_16_16_18_expect__8(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,16,18]), (8))

    def test_max_occurrences_with_10_20_20_30_40_90_80_50_30_20_50_10_expect__20(self):
        self.assertEqual(max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10]), (20))

