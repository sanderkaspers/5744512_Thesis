import unittest
from datasets.GPT_4.Few_shot.programs.program_094 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 9) # Subrange from index 1 to 3)

    def test_case_2(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 0, 4), 15) # Entire range)

    def test_case_3(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 2), 3) # Single element subrange)

    def test_case_4(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 0, 0), 1) # Subrange with single first element)

    def test_case_5(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 4, 4), 5) # Subrange with single last element)

    def test_case_6(self):
        self.assertEqual(sum_range_list([10, 20, 30, 40], 1, 2), 50) # Middle subrange)

    def test_case_7(self):
        try:
            sum_range_list([], 0, 1)   # Empty list
        except IndexError:
            print("Passed: IndexError for empty list.")

    def test_case_8(self):
        self.assertEqual(sum_range_list([5, 5, 5, 5], 1, 3), 15) # Subrange with identical elements)

