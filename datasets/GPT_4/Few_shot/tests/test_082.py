import unittest
from datasets.GPT_4.Few_shot.programs.program_082 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3) # All elements match)

    def test_case_2(self):
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [7, 8, 9]), 0) # No elements match)

    def test_case_3(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 5, 3], [1, 2, 3]), 2) # Partial match)

    def test_case_4(self):
        self.assertEqual(count_samepair([], [], []), 0) # Empty lists)

    def test_case_5(self):
        self.assertEqual(count_samepair([1, 1, 1], [1, 1, 1], [1, 1, 1]), 3) # All identical elements)

    def test_case_6(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 1, 1]), 2) # Two matches)

    def test_case_7(self):
        self.assertEqual(count_samepair([1, 2], [1, 2], [1, 2]), 2) # Shorter lists)

    def test_case_8(self):
        self.assertEqual(count_samepair([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]), 4) # Longer lists, all match)

