import unittest
from datasets.GPT_4.Few_shot.programs.program_014 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(smallest_num([1]), 1) # Single element)

    def test_case_2(self):
        self.assertEqual(smallest_num([1, 2, 3, 4, 5]), 1) # Ascending order)

    def test_case_3(self):
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5]), -5) # All negative numbers)

    def test_case_4(self):
        self.assertEqual(smallest_num([100, 99, 98, 97, 96]), 96) # Descending order)

    def test_case_5(self):
        self.assertEqual(smallest_num([3, 3, 3, 3, 3]), 3) # All identical elements)

    def test_case_6(self):
        self.assertEqual(smallest_num([2, -3, 4, -1, 5, -6]), -6) # Mix of positive and negative numbers)

    def test_case_7(self):
        self.assertEqual(smallest_num([1, 2, 3, 0]), 0) # Includes zero)

    def test_case_8(self):
        self.assertEqual(smallest_num([10, 20, 30, 40, 50, 5, 60, 70, 80, 90, 100]), 5) # Large list)

