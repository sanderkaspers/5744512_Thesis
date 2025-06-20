import unittest
from datasets.GPT_4.Few_shot.programs.program_007 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(test_duplicate([]), False)

    def test_case_2(self):
        self.assertEqual(test_duplicate([1, 2, 3, 4, 5]), False)

    def test_case_3(self):
        self.assertEqual(test_duplicate([1, 2, 2, 3, 4, 5]), True)

    def test_case_4(self):
        self.assertEqual(test_duplicate([1, 1, 1, 1]), True)

    def test_case_5(self):
        self.assertEqual(test_duplicate(["a", "b", "c", "a"]), True)

    def test_case_6(self):
        self.assertEqual(test_duplicate([1, 2, 3, "a", "b", "c", "a"]), True)

    def test_case_7(self):
        self.assertEqual(test_duplicate([1, 2, 3, "a", "b", "c"]), False)

    def test_case_8(self):
        self.assertEqual(test_duplicate([0, 0, 0]), True)

