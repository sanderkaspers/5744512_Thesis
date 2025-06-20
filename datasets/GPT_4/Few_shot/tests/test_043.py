import unittest
from datasets.GPT_4.Few_shot.programs.program_043 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Find_Min_Length(["short", "tiny", "miniscule"]), "tiny") # Smallest string)

    def test_case_2(self):
        self.assertEqual(Find_Min_Length(["same", "size", "size"]), "same") # All same length)

    def test_case_3(self):
        try:
            Find_Min_Length([])   # Empty list
        except ValueError:
            print("Passed: ValueError for empty list.")

    def test_case_4(self):
        self.assertEqual(Find_Min_Length(["single"]), "single") # Single string in list)

    def test_case_5(self):
        self.assertEqual(Find_Min_Length(["short", "longer", "longest"]), "short") # Mixed lengths)

    def test_case_6(self):
        self.assertEqual(Find_Min_Length(["", "nonempty", "longest"]), "") # Empty string in list)

    def test_case_7(self):
        self.assertEqual(Find_Min_Length(["aaa", "aa", "aaaa"]), "aa") # Close lengths)

    def test_case_8(self):
        self.assertEqual(Find_Min_Length(["a", "bb", "ccc", "dddd"]), "a") # Incrementing length)

