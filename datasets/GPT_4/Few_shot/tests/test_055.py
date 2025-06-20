import unittest
from datasets.GPT_4.Few_shot.programs.program_055 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(merge_sorted_list([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]) # Standard case)

    def test_case_2(self):
        self.assertEqual(merge_sorted_list([1, 2, 3], [1, 2, 3]), [1, 1, 2, 2, 3, 3]) # Identical elements)

    def test_case_3(self):
        self.assertEqual(merge_sorted_list([1, 3, 5], []), [1, 3, 5]) # One empty list)

    def test_case_4(self):
        self.assertEqual(merge_sorted_list([], [2, 4, 6]), [2, 4, 6]) # Other empty list)

    def test_case_5(self):
        self.assertEqual(merge_sorted_list([10, 20], [1, 2, 3]), [1, 2, 3, 10, 20]) # Different ranges)

    def test_case_6(self):
        self.assertEqual(merge_sorted_list([1], [2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6]) # Single element in first list)

    def test_case_7(self):
        self.assertEqual(merge_sorted_list([1, 3, 5], [2]), [1, 2, 3, 5]) # Single element in second list)

    def test_case_8(self):
        self.assertEqual(merge_sorted_list([1, 3, 3, 5], [2, 4, 4, 6]), [1, 2, 3, 3, 4, 4, 5, 6]) # Lists with duplicate elements)

