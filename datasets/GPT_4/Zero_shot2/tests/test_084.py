import unittest
from datasets.GPT_4.Zero_shot2.programs.program_084 import *

class TestVersion(unittest.TestCase):
    def test_diff_1(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4]), 4)

    def test_diff_2(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3]), 2)

    def test_diff_3(self):
        self.assertEqual(max_Abs_Diff([-4, -2, 0, 2, 4]), 8)

    def test_diff_4(self):
        self.assertEqual(max_Abs_Diff([5, 5, 5, 5]), 0)

    def test_diff_5(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5]), 6)

    def test_diff_6(self):
        self.assertEqual(max_Abs_Diff([5, 4, 3, 2, 1]), 6)

    def test_diff_7(self):
        self.assertEqual(max_Abs_Diff([]), 0)

    def test_diff_8(self):
        self.assertEqual(max_Abs_Diff([42]), 0)

    def test_diff_9(self):
        self.assertEqual(max_Abs_Diff([100, 1]), 99)

    def test_diff_10(self):
        self.assertEqual(max_Abs_Diff([1, 1, 2, 2, 3, 3]), 4)

