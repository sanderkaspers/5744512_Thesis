import unittest
from datasets.mbpp.programs.program_023 import *

class TestVersion(unittest.TestCase):
    def test_comb_sort_with_5_15_37_25_79_expect__5(self):
        self.assertEqual(comb_sort([5, 15, 37, 25, 79]), [5, 15, 25, 37, 79])

    def test_comb_sort_with_41_32_15_19_22_expect__15(self):
        self.assertEqual(comb_sort([41, 32, 15, 19, 22]), [15, 19, 22, 32, 41])

    def test_comb_sort_with_99_15_13_47_expect__13(self):
        self.assertEqual(comb_sort([99, 15, 13, 47]), [13, 15, 47, 99])

