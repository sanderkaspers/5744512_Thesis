import unittest
from datasets.mbpp.programs.program_068 import *

class TestVersion(unittest.TestCase):
    def test_sum_with_10_15_expect_6(self):
        self.assertEqual(sum(10,15), 6)

    def test_sum_with_100_150_expect_93(self):
        self.assertEqual(sum(100,150), 93)

    def test_sum_with_4_6_expect_3(self):
        self.assertEqual(sum(4,6), 3)

