import unittest
from datasets.GPT_4.Few_shot.programs.program_080 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(extract_singly([1, 2, 3, 4]), [1, 2, 3, 4]) # All unique elements)

    def test_case_2(self):
        self.assertEqual(extract_singly([1, 1, 2, 2]), []) # All duplicate elements)

    def test_case_3(self):
        self.assertEqual(extract_singly([1, 2, 2, 3, 4, 4]), [1, 3]) # Mixed unique and duplicate)

    def test_case_4(self):
        self.assertEqual(extract_singly([]), []) # Empty list)

    def test_case_5(self):
        self.assertEqual(extract_singly([5, 6, 5, 7, 8]), [6, 7, 8]) # Some unique, some duplicate)

    def test_case_6(self):
        self.assertEqual(extract_singly([1]), [1]) # Single element)

    def test_case_7(self):
        self.assertEqual(extract_singly([10, 20, 30, 10, 40, 50, 30]), [20, 40, 50]) # Complex case)

    def test_case_8(self):
        self.assertEqual(extract_singly(["a", "b", "a", "c", "b", "d"]), ["c", "d"]) # Strings instead of numbers)

