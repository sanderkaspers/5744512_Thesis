import unittest
from datasets.GPT_4.Few_shot.programs.program_068 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sum(1, 5), 15) # 1+2+3+4+5)

    def test_case_2(self):
        self.assertEqual(sum(-5, 5), 0) # Sum from -5 to 5)

    def test_case_3(self):
        self.assertEqual(sum(3, 3), 3) # Single number)

    def test_case_4(self):
        self.assertEqual(sum(5, 1), 0) # Reversed range (no sum))

    def test_case_5(self):
        self.assertEqual(sum(0, 10), 55) # Sum from 0 to 10)

    def test_case_6(self):
        self.assertEqual(sum(-10, -1), -55) # Sum of negative numbers)

    def test_case_7(self):
        self.assertEqual(sum(-3, 3), 0) # Mixed positive and negative)

    def test_case_8(self):
        self.assertEqual(sum(100, 100), 100) # Single large number)

