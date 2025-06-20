import unittest
from datasets.mbpp.programs.program_086 import *

class TestVersion(unittest.TestCase):
    def test_remove_elements_with_1_2_3_4_5_6_7_8_9_10_2_4_6_8_expect__1(self):
        self.assertEqual(remove_elements([1,2,3,4,5,6,7,8,9,10],[2,4,6,8]), [1, 3, 5, 7, 9, 10])

    def test_remove_elements_with_1_2_3_4_5_6_7_8_9_10_1_3_5_7_expect__2(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 3, 5, 7]), [2, 4, 6, 8, 9, 10])

    def test_remove_elements_with_1_2_3_4_5_6_7_8_9_10_5_7_expect__1(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[5,7]), [1, 2, 3, 4, 6, 8, 9, 10])

