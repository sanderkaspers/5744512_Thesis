import unittest
from datasets.o3.programs.program_084 import *

class TestVersion(unittest.TestCase):
    def test_max_Abs_Diff_ascending(self):
        self.assertEqual(max_Abs_Diff([1,2,3,4]), 3)

    def test_max_Abs_Diff_descending(self):
        self.assertEqual(max_Abs_Diff([9,5,1]), 8)

    def test_max_Abs_Diff_single_element(self):
        self.assertEqual(max_Abs_Diff([7]), 0)

    def test_max_Abs_Diff_identical_numbers(self):
        self.assertEqual(max_Abs_Diff([5,5,5]), 0)

    def test_max_Abs_Diff_negative_numbers(self):
        self.assertEqual(max_Abs_Diff([-3,-10,-1]), 9)

    def test_max_Abs_Diff_floats(self):
        self.assertAlmostEqual(max_Abs_Diff([1.1, 2.9, 2.0]), 1.8)

    def test_max_Abs_Diff_empty_list(self):
        with self.assertRaises(IndexError):
            max_Abs_Diff([])

