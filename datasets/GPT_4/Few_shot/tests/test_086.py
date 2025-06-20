import unittest
from datasets.GPT_4.Few_shot.programs.program_086 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(remove_elements([1, 2, 3, 4], [2, 4]), [1, 3]) # Overlapping elements)

    def test_case_2(self):
        self.assertEqual(remove_elements([1, 2, 3], [4, 5, 6]), [1, 2, 3]) # No common elements)

    def test_case_3(self):
        self.assertEqual(remove_elements([1, 2, 3], []), [1, 2, 3]) # Second list empty)

    def test_case_4(self):
        self.assertEqual(remove_elements([], [1, 2, 3]), []) # First list empty)

    def test_case_5(self):
        self.assertEqual(remove_elements([1, 2, 3, 4], [1, 2, 3, 4]), []) # All elements removed)

    def test_case_6(self):
        self.assertEqual(remove_elements(["apple", "banana"], ["banana"]), ["apple"]) # String elements)

    def test_case_7(self):
        self.assertEqual(remove_elements([1, 1, 2, 2], [1]), [2, 2]) # Duplicate elements in first list)

    def test_case_8(self):
        self.assertEqual(remove_elements([1, 2, 3], [1, 2, 3, 4]), []) # All elements match and removed)

