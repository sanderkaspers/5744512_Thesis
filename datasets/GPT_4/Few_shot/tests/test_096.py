import unittest
from datasets.GPT_4.Few_shot.programs.program_096 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_occurance("ababcab"), 2) # Two occurrences of "ab")

    def test_case_2(self):
        self.assertEqual(count_occurance("abcdef"), 1) # Single occurrence at the beginning)

    def test_case_3(self):
        self.assertEqual(count_occurance("xyzxyz"), 0) # No "ab" occurrences)

    def test_case_4(self):
        self.assertEqual(count_occurance("ababab"), 3) # Overlapping "ab" occurrences)

    def test_case_5(self):
        self.assertEqual(count_occurance("ba"), 0) # "ab" not present)

    def test_case_6(self):
        self.assertEqual(count_occurance(""), 0) # Empty string)

    def test_case_7(self):
        self.assertEqual(count_occurance("ab"), 1) # Exact match)

    def test_case_8(self):
        self.assertEqual(count_occurance("cab"), 1) # "ab" at the end)

