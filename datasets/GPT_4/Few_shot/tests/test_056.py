import unittest
from datasets.GPT_4.Few_shot.programs.program_056 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(odd_Equivalent([1, 3, 5, 7], 4), 4) # All odd numbers)

    def test_case_2(self):
        self.assertEqual(odd_Equivalent([2, 4, 6, 8], 4), 0) # No odd numbers)

    def test_case_3(self):
        self.assertEqual(odd_Equivalent([1, 2, 3, 4, 5], 5), 3) # Mixed odd and even numbers)

    def test_case_4(self):
        self.assertEqual(odd_Equivalent([], 0), 0) # Empty list)

    def test_case_5(self):
        self.assertEqual(odd_Equivalent([1], 1), 1) # Single odd number)

    def test_case_6(self):
        self.assertEqual(odd_Equivalent([2], 1), 0) # Single even number)

    def test_case_7(self):
        self.assertEqual(odd_Equivalent([1, 1, 1, 1], 4), 4) # All identical odd numbers)

    def test_case_8(self):
        self.assertEqual(odd_Equivalent([2, 3, 4, 5, 6, 7, 8, 9], 8), 4) # Larger mixed list)

