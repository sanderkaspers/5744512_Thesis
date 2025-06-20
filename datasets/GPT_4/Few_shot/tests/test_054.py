import unittest
from datasets.GPT_4.Few_shot.programs.program_054 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5)), (4, 5, 1, 2, 3))   # Standard case)

    def test_case_2(self):
        self.assertEqual(add_lists([], (1, 2, 3)), (1, 2, 3))   # Empty list)

    def test_case_3(self):
        self.assertEqual(add_lists([1, 2, 3], ()), (1, 2, 3) )  # Empty tuple)

    def test_case_4(self):
        self.assertEqual(add_lists([1, 'a', 2.5], (4, 5)), (4, 5, 1, 'a', 2.5) )  # Mixed elements)

    def test_case_5(self):
        self.assertEqual(add_lists([], ()), () )  # Both empty)

    def test_case_6(self):
        self.assertEqual(add_lists(['apple'], ('banana', 'cherry')), ('banana', 'cherry', 'apple'))   # Strings)

    def test_case_7(self):
        self.assertEqual(add_lists([True, False], (None,)), (None, True, False) )  # Boolean and None)

    def test_case_8(self):
        self.assertEqual(add_lists([0], (-1, 1)), (-1, 1, 0))   # Single element list)

