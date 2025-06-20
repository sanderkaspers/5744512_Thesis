import unittest
from datasets.mbpp.programs.program_056 import *

class TestVersion(unittest.TestCase):
    def test_odd_Equivalent_with__011001__6_expect_3(self):
        self.assertEqual(odd_Equivalent("011001",6), 3)

    def test_odd_Equivalent_with__11011__5_expect_4(self):
        self.assertEqual(odd_Equivalent("11011",5), 4)

    def test_odd_Equivalent_with__1010__4_expect_2(self):
        self.assertEqual(odd_Equivalent("1010",4), 2)

