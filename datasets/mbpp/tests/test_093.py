import unittest
from datasets.mbpp.programs.program_093 import *

class TestVersion(unittest.TestCase):
    def test_frequency_with_1_2_3_4_expect_0(self):
        self.assertEqual(frequency([1,2,3],4), 0)

    def test_frequency_with_1_2_2_3_3_3_4_3_expect_3(self):
        self.assertEqual(frequency([1,2,2,3,3,3,4],3), 3)

    def test_frequency_with_0_1_2_3_1_2_1_expect_2(self):
        self.assertEqual(frequency([0,1,2,3,1,2],1), 2)

