import unittest
from datasets.mbpp.programs.program_049 import *

class TestVersion(unittest.TestCase):
    def test_kth_element_with_12_3_5_7_19_2_expect_3(self):
        self.assertEqual(kth_element([12,3,5,7,19], 2), 3)

    def test_kth_element_with_17_24_8_23_3_expect_8(self):
        self.assertEqual(kth_element([17,24,8,23], 3), 8)

    def test_kth_element_with_16_21_25_36_4_4_expect_36(self):
        self.assertEqual(kth_element([16,21,25,36,4], 4), 36)

