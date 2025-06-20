import unittest
from datasets.mbpp.programs.program_010 import *

class TestVersion(unittest.TestCase):
    def test_find_Max_Num_with_1_2_3_3_expect_321(self):
        self.assertEqual(find_Max_Num([1,2,3]), 321)

    def test_find_Max_Num_with_4_5_6_1_4_expect_6541(self):
        self.assertEqual(find_Max_Num([4,5,6,1]), 6541)

    def test_find_Max_Num_with_1_2_3_9_4_expect_9321(self):
        self.assertEqual(find_Max_Num([1,2,3,9]), 9321)

