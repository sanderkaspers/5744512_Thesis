import unittest
from datasets.GPT_4.Few_shot.programs.program_022 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_equal_tuple([(1, 1, 1), (2, 2, 2)]), (1, 1, 1))   # First equal tuple

    def test_case_2(self):
        self.assertEqual(find_equal_tuple([(1, 2, 3), (4, 4, 4), (5, 5, 5)]), (4, 4, 4))   # Middle equal tuple

    def test_case_3(self):
        self.assertEqual(find_equal_tuple([(1, 2, 3), (4, 5, 6)]), (1, 2, 3))   # No equal tuples

    def test_case_4(self):
        self.assertEqual(find_equal_tuple([]), 0) # Empty list

    def test_case_5(self):
        self.assertEqual(find_equal_tuple([(0, 0, 0), (1, 1, 1)]), (0, 0, 0))   # Zero tuple)

    def test_case_6(self):
        self.assertEqual(find_equal_tuple([(1, 2), (2, 2), (3, 3, 3)]), (2, 2))   # Mixed tuple sizes)

    def test_case_7(self):
        self.assertEqual(find_equal_tuple([(3, 3, 3)]), (3, 3, 3))   # Single tuple)

    def test_case_8(self):
        self.assertEqual(find_equal_tuple([(4,), (4, 4), (4, 4, 4)]), (4,))   # Single element tuple)

