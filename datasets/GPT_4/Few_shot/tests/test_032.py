import unittest
from datasets.GPT_4.Few_shot.programs.program_032 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sequence(1), 1) # Edge case n = 1)

    def test_case_2(self):
        self.assertEqual(sequence(2), 1) # Edge case n = 2)

    def test_case_3(self):
        self.assertEqual(sequence(3), 2) # Small value)

    def test_case_4(self):
        self.assertEqual(sequence(4), 3) # Small value)

    def test_case_5(self):
        self.assertEqual(sequence(5), 5) # Small value)

    def test_case_6(self):
        self.assertEqual(sequence(10), 55) # Medium value)

    def test_case_7(self):
        # This test case might be slow depending on the implementation.
        self.assertEqual(sequence(20), 6765) # Large value)

    def test_case_8(self):
        # The function does not naturally handle negative n, so an invalid input case.
        try:
            sequence(-5)
        except RecursionError:
            print("Passed: RecursionError for negative input.")


