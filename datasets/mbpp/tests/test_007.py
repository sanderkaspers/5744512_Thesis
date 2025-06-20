import unittest
from datasets.mbpp.programs.program_007 import *

class TestVersion(unittest.TestCase):
    def test_test_duplicate_with__1_2_3_4_5__expect_False(self):
        self.assertEqual(test_duplicate(([1,2,3,4,5])), False)

    def test_test_duplicate_with__1_2_3_4_4__expect_True(self):
        self.assertEqual(test_duplicate(([1,2,3,4, 4])), True)

    def test_test_duplicate_with_1_1_2_2_3_3_4_4_5_expect_True(self):
        self.assertEqual(test_duplicate([1,1,2,2,3,3,4,4,5]), True)

