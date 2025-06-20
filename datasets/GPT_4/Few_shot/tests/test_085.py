import unittest
from datasets.GPT_4.Few_shot.programs.program_085 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_solution(1, 2, 5), 2) # Valid solution)

    def test_case_2(self):
        self.assertEqual(find_solution(0, 1, 10), 10) # Simple case)

    def test_case_3(self):
        self.assertEqual(find_solution(5, 5, 20), 3) # Larger numbers)

    def test_case_4(self):
        self.assertEqual(find_solution(2, 3, 7), None) # No valid solution)

    def test_case_5(self):
        self.assertEqual(find_solution(0, 2, 0), 0) # Edge case with n = 0)

    def test_case_6(self):
        self.assertEqual(find_solution(-1, 2, 3), 2) # Negative a)

    def test_case_7(self):
        self.assertEqual(find_solution(1, -2, -5), 3) # Negative b)

    def test_case_8(self):
        self.assertEqual(find_solution(-1, -2, -5), 2) # Both negative)

