import unittest
from datasets.mbpp.programs.program_082 import *

class TestVersion(unittest.TestCase):
    def test_count_samepair_with_1_2_3_4_5_6_7_8_2_2_3_1_2_6_7_9_2_1_3_1_2_6_7_9_expect_(self):
        self.assertEqual(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]), 3)

    def test_count_samepair_with_1_2_3_4_5_6_7_8_2_2_3_1_2_6_7_8_2_1_3_1_2_6_7_8_expect_(self):
        self.assertEqual(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8]), 4)

    def test_count_samepair_with_1_2_3_4_2_6_7_8_2_2_3_1_2_6_7_8_2_1_3_1_2_6_7_8_expect_(self):
        self.assertEqual(count_samepair([1,2,3,4,2,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8]), 5)

