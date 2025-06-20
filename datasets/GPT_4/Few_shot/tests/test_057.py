import unittest
from datasets.GPT_4.Few_shot.programs.program_057 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), {3}) # One common element)

    def test_case_2(self):
        self.assertEqual(common_in_nested_lists([[1, 2], [3, 4], [5, 6]]), set())   # No common elements)

    def test_case_3(self):
        self.assertEqual(common_in_nested_lists([[1, 2], [2, 1], [1, 2]]), {1, 2}) # All elements common)

    def test_case_4(self):
        self.assertEqual(common_in_nested_lists([[], [1, 2], [2, 3]]), set())   # One empty list)

    def test_case_5(self):
        self.assertEqual(common_in_nested_lists([[], []]), set())  # All empty lists)

    def test_case_6(self):
        self.assertEqual(common_in_nested_lists([[1, 1, 1], [1, 1], [1]]), {1}) # Repeated elements in lists)

    def test_case_7(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3], [3]]), {3}) # Decreasing length)

    def test_case_8(self):
        self.assertEqual(common_in_nested_lists([[1, 2, 3], [2, 3, 4], [1, 3, 5]]), {3}) # One common element)

