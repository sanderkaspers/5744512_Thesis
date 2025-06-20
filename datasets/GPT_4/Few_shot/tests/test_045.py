import unittest
from datasets.GPT_4.Few_shot.programs.program_045 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(frequency_lists([[1, 2], [2, 3], [1, 1]]), [[1, 3], [2, 2], [3, 1]]) # Repeated elements)

    def test_case_2(self):
        self.assertEqual(frequency_lists([[1], [2], [3]]), [[1, 1], [2, 1], [3, 1]]) # Unique elements)

    def test_case_3(self):
        self.assertEqual(frequency_lists([[], []]), []) # Empty nested lists)

    def test_case_4(self):
        self.assertEqual(frequency_lists([["a", "b"], ["a", "c"], ["a", "b", "c"]]), [['a', 3], ['b', 2], ['c', 2]]) # Strings)

    def test_case_5(self):
        self.assertEqual(frequency_lists([[None], [None, None]]), [[None, 3]]) # None values)

    def test_case_6(self):
        self.assertEqual(frequency_lists([[True, False], [True], [False, False]]), [[False, 3], [True, 2]]) # Boolean values)

    def test_case_7(self):
        self.assertEqual(frequency_lists([[1, 1, 1], [2, 2], [3]]), [[1, 3], [2, 2], [3, 1]]) # Repeated in a single sublist)

    def test_case_8(self):
        self.assertEqual(frequency_lists([[1.5], [2.5], [1.5, 2.5, 2.5]]), [[1.5, 2], [2.5, 3]]) # Floating-point numbers)

