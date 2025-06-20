import unittest
from datasets.GPT_4.Few_shot.programs.program_093 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(frequency([1, 2, 3, 1, 1, 4], 1), 3) # Element appears multiple times)

    def test_case_2(self):
        self.assertEqual(frequency([1, 2, 3, 4, 5], 6), 0) # Element not present)

    def test_case_3(self):
        self.assertEqual(frequency([], 1), 0) # Empty list)

    def test_case_4(self):
        self.assertEqual(frequency(["a", "b", "a", "c"], "a"), 2) # String elements)

    def test_case_5(self):
        self.assertEqual(frequency([True, False, True], True), 2) # Boolean elements)

    def test_case_6(self):
        self.assertEqual(frequency([1, 2, 3, 4], 3), 1) # Single occurrence)

    def test_case_7(self):
        self.assertEqual(frequency([None, None, None], None), 3) # None elements)

    def test_case_8(self):
        self.assertEqual(frequency([1.1, 2.2, 1.1, 3.3], 1.1), 2) # Float elements)

