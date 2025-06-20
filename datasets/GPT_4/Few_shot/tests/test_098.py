import unittest
from datasets.GPT_4.Few_shot.programs.program_098 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_majority([1, 1, 1, 2, 2], 5, 1), True) # 1 is a majority)

    def test_case_2(self):
        self.assertEqual(is_majority([1, 2, 3, 4, 5], 5, 2), False) # 2 is not a majority)

    def test_case_3(self):
        self.assertEqual(is_majority([1, 1, 1, 1, 2, 2, 2], 7, 1), True) # 1 is a majority with an odd count)

    def test_case_4(self):
        self.assertEqual(is_majority([1, 1, 2, 2, 2], 5, 2), True) # 2 is a majority)

    def test_case_5(self):
        self.assertEqual(is_majority([1, 2, 3], 3, 4), False) # 4 is not present)

    def test_case_6(self):
        self.assertEqual(is_majority([1, 2, 3], 3, 1), False) # 1 is not a majority)

    def test_case_7(self):
        self.assertEqual(is_majority([1, 1, 1, 1, 1], 5, 1), True) # 1 is a clear majority)

    def test_case_8(self):
        self.assertEqual(is_majority([1, 2], 2, 2), False) # 2 is not a majority in a small array)

