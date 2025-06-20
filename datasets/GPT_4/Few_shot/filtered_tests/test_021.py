import unittest
from datasets.GPT_4.Few_shot.programs.program_021 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_sublist([1, 2, 3, 4, 5], [2, 3]), True) # Sublist)

    def test_case_2(self):
        self.assertEqual(is_sublist([1, 2, 3, 4, 5], [3, 2]), False) # Not a sublist)

    def test_case_3(self):
        self.assertEqual(is_sublist([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), True) # Identical lists)

    def test_case_4(self):
        self.assertEqual(is_sublist([], []), True) # Both lists empty)

    def test_case_5(self):
        self.assertEqual(is_sublist([1, 2, 3], []), True) # `s` is empty)

    def test_case_6(self):
        self.assertEqual(is_sublist([], [1, 2, 3]), False) # `l` is empty)

    def test_case_7(self):
        self.assertEqual(is_sublist([1, 2, 3, 4, 5], [6, 7]), False) # `s` not in `l`)

    def test_case_8(self):
        self.assertEqual(is_sublist([1, 2, 3, 4, 5], [5]), True) # Single element sublist)

