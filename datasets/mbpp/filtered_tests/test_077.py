import unittest
from datasets.mbpp.programs.program_077 import *

class TestVersion(unittest.TestCase):
    def test_zero_count_with_0s_expect_0_18(self):
        self.assertEqual(round(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 2), 0.18)

    def test_zero_count_with_no_zeros_expect_0_00(self):
        self.assertEqual(round(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 2), 0.00)

    def test_zero_count_with_all_nonzero_expect_0_00(self):
        self.assertEqual(round(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 2), 0.00)

