import unittest
from datasets.GPT_4.Few_shot.programs.program_018 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(pos_count([1, 2, 3, 4, 5]), 5) # All positive)

    def test_case_2(self):
        self.assertEqual(pos_count([-1, -2, -3, -4, -5]), 0) # All negative)

    def test_case_3(self):
        self.assertEqual(pos_count([0, 0, 0, 0, 0]), 0) # All zeros)

    def test_case_4(self):
        self.assertEqual(pos_count([1, -2, 3, 0, -4, 5]), 3) # Mixed list)

    def test_case_5(self):
        self.assertEqual(pos_count([]), 0) # Empty list)

    def test_case_6(self):
        self.assertEqual(pos_count([-1, 2, -3, 4, 5, -6]), 3) # Mixed list with positives and negatives)

    def test_case_7(self):
        self.assertEqual(pos_count([1]), 1) # Single positive element)

    def test_case_8(self):
        self.assertEqual(pos_count([-1]), 0) # Single negative element)

