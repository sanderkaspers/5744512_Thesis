import unittest
from datasets.mbpp.programs.program_037 import *

class TestVersion(unittest.TestCase):
    def test_closest_num_with_11_expect_10(self):
        self.assertEqual(closest_num(11), 10)

    def test_closest_num_with_7_expect_6(self):
        self.assertEqual(closest_num(7), 6)

    def test_closest_num_with_12_expect_11(self):
        self.assertEqual(closest_num(12), 11)

