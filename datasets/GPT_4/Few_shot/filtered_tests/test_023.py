import unittest
from datasets.GPT_4.Few_shot.programs.program_023 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(comb_sort([5, 3, 2, 8, 7]), [2, 3, 5, 7, 8]) # Unsorted list)

    def test_case_2(self):
        self.assertEqual(comb_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]) # Already sorted list)

    def test_case_3(self):
        self.assertEqual(comb_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]) # Reverse sorted list)

    def test_case_4(self):
        self.assertEqual(comb_sort([3, 3, 3, 3]), [3, 3, 3, 3]) # List with identical elements)

    def test_case_5(self):
        self.assertEqual(comb_sort([]), []) # Empty list)

    def test_case_6(self):
        self.assertEqual(comb_sort([1]), [1]) # Single element list)

    def test_case_7(self):
        self.assertEqual(comb_sort([9, -1, 4, -10, 8]), [-10, -1, 4, 8, 9]) # List with negative numbers)

    def test_case_8(self):
        self.assertEqual(comb_sort([2, 2, 2, 2, 1, 1, 1, 1]), [1, 1, 1, 1, 2, 2, 2, 2]) # List with duplicates)

