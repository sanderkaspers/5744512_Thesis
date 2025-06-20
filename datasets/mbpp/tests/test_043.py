import unittest
from datasets.mbpp.programs.program_043 import *

class TestVersion(unittest.TestCase):
    def test_Find_Min_Length_with_1_1_2_expect_1(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

    def test_Find_Min_Length_with_1_2_1_2_3_1_2_3_4_expect_2(self):
        self.assertEqual(Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]), 2)

    def test_Find_Min_Length_with_3_3_3_4_4_4_4_expect_3(self):
        self.assertEqual(Find_Min_Length([[3,3,3],[4,4,4,4]]), 3)

