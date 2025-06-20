import unittest
from datasets.mbpp.programs.program_075 import *

class TestVersion(unittest.TestCase):
    def test_sum_negativenum_with_2_4__6__9_11__12_14__5_17_expect__32(self):
        self.assertEqual(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]), -32)

    def test_sum_negativenum_with_10_15__14_13__18_12__20_expect__52(self):
        self.assertEqual(sum_negativenum([10,15,-14,13,-18,12,-20]), -52)

    def test_sum_negativenum_with_19__65_57_39_152__639_121_44_90__190_expect__894(self):
        self.assertEqual(sum_negativenum([19, -65, 57, 39, 152,-639, 121, 44, 90, -190]), -894)

