import unittest
from datasets.GPT_4.Few_shot.programs.program_081 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(pancake_sort([3, 2, 4, 1]), [3, 4, 2, 3, 1, 2]) # Simple unsorted list)

    def test_case_2(self):
        self.assertEqual(pancake_sort([1, 2, 3, 4]), []) # Already sorted list)

    def test_case_3(self):
        self.assertEqual(pancake_sort([4, 3, 2, 1]), [4, 4, 3, 3, 2, 2]) # Reverse sorted list)

    def test_case_4(self):
        self.assertEqual(pancake_sort([1]), []) # Single element list)

    def test_case_5(self):
        self.assertEqual(pancake_sort([1, 2, 3, 4, 5]), []) # Already sorted, multiple elements)

    def test_case_6(self):
        self.assertEqual(pancake_sort([]), []) # Empty list)

    def test_case_7(self):
        self.assertEqual(pancake_sort([5, 4, 3, 2, 1]), [5, 5, 4, 4, 3, 3, 2, 2]) # Reverse sorted, larger list)

    def test_case_8(self):
        self.assertEqual(pancake_sort([3, 3, 3, 3, 3]), []) # All elements the same)

