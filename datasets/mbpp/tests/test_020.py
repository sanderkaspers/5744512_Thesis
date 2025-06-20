import unittest
from datasets.mbpp.programs.program_020 import *

class TestVersion(unittest.TestCase):
    def test_is_Monotonic_with_6_5_4_4_expect_True(self):
        self.assertEqual(is_Monotonic([6, 5, 4, 4]), True)

    def test_is_Monotonic_with_1_2_2_3_expect_True(self):
        self.assertEqual(is_Monotonic([1, 2, 2, 3]), True)

    def test_is_Monotonic_with_1_3_2_expect_False(self):
        self.assertEqual(is_Monotonic([1, 3, 2]), False)

