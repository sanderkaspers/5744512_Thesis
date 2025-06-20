import unittest
from datasets.mbpp.programs.program_014 import *

class TestVersion(unittest.TestCase):
    def test_smallest_num_with_10_20_1_45_99_expect_1(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)

    def test_smallest_num_with_1_2_3_expect_1(self):
        self.assertEqual(smallest_num([1, 2, 3]), 1)

    def test_smallest_num_with_45_46_50_60_expect_45(self):
        self.assertEqual(smallest_num([45, 46, 50, 60]), 45)

