import unittest
from datasets.GPT_4.Few_shot.programs.program_042 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(index_min_value_tuples([(1, 2), (3, 0), (5, 5)], 1), 1) # Minimum at index 1)

    def test_case_2(self):
        self.assertEqual(index_min_value_tuples([(1, 2), (3, 0), (5, 5)], 0), 0) # Minimum at index 0)

    def test_case_3(self):
        self.assertEqual(index_min_value_tuples([(1, 1), (1, 1), (1, 1)], 1), 0) # All identical values)

    def test_case_4(self):
        self.assertEqual(index_min_value_tuples([(10, 20)], 0), 0) # Single tuple)

    def test_case_5(self):
        try:
            index_min_value_tuples([], 0)   # Empty list
        except ValueError:
            print("Passed: ValueError for empty list.")

    def test_case_6(self):
        self.assertEqual(index_min_value_tuples([(10, 20), (5, 25), (15, 10)], 1), 2) # Minimum at last tuple)

    def test_case_7(self):
        self.assertEqual(index_min_value_tuples([(0, 1), (2, 3), (4, 5)], 1), 0) # Minimum at first tuple, index 1)

    def test_case_8(self):
        self.assertEqual(index_min_value_tuples([(2, 1), (1, 2), (3, 0)], 1), 2) # Minimum value at different index in each tuple)

