import unittest
from datasets.mbpp.programs.program_036 import *

class TestVersion(unittest.TestCase):
    def test_freq_count_with_10_10_10_10_20_20_20_20_40_40_50_50_30_expect__10_4(self):
        self.assertEqual(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]), ({10: 4, 20: 4, 40: 2, 50: 2, 30: 1}))

    def test_freq_count_with_1_2_3_4_3_2_4_1_3_1_4_expect__1_3(self):
        self.assertEqual(freq_count([1,2,3,4,3,2,4,1,3,1,4]), ({1:3, 2:2,3:3,4:3}))

    def test_freq_count_with_5_6_7_4_9_10_4_5_6_7_9_5_expect__10_1(self):
        self.assertEqual(freq_count([5,6,7,4,9,10,4,5,6,7,9,5]), ({10:1,5:3,6:2,7:2,4:2,9:2}))

