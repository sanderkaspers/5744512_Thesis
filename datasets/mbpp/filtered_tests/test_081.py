import unittest
from datasets.mbpp.programs.program_081 import *

class TestVersion(unittest.TestCase):
    def test_pancake_sort_with_15_79_25_38_69_expect__15(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

    def test_pancake_sort_with_98_12_54_36_85_expect__12(self):
        self.assertEqual(pancake_sort([98, 12, 54, 36, 85]), [12, 36, 54, 85, 98])

    def test_pancake_sort_with_41_42_32_12_23_expect__12(self):
        self.assertEqual(pancake_sort([41, 42, 32, 12, 23]), [12, 23, 32, 41, 42])

