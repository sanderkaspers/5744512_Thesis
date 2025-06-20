import unittest
from datasets.mbpp.programs.program_077 import *

class TestVersion(unittest.TestCase):
    def test_zero_count_with_0_1_2__1__5_6_0__3__2_3_4_6_8_expect_0_15(self):
        self.assertEqual(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.15, places=2)

    def test_zero_count_with_2_1_2__1__5_6_4__3__2_3_4_6_8_expect_0_00(self):
        self.assertEqual(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, places=2)

    def test_zero_count_with_2_4__6__9_11__12_14__5_17_expect_0_00(self):
        self.assertEqual(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, places=2)

