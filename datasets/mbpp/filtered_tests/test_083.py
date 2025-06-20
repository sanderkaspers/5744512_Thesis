import unittest
from datasets.mbpp.programs.program_083 import *

class TestVersion(unittest.TestCase):
    def test_find_lists_with__1_2_3_4_5_6_7_8__expect_2(self):
        self.assertEqual(find_lists(([1, 2, 3, 4], [5, 6, 7, 8])), 2)

    def test_find_lists_with__1_2_3_4_5_6__expect_3(self):
        self.assertEqual(find_lists(([1, 2], [3, 4], [5, 6])), 3)

    def test_find_lists_with__9_8_7_6_5_4_3_2_1__expect_1(self):
        self.assertEqual(find_lists(([9, 8, 7, 6, 5, 4, 3, 2, 1])), 1)

