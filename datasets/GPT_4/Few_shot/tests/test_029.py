import unittest
from datasets.GPT_4.Few_shot.programs.program_029 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(tetrahedral_number(0), 0) # Edge case n = 0)

    def test_case_2(self):
        self.assertEqual(tetrahedral_number(1), 1) # Small value)

    def test_case_3(self):
        self.assertEqual(tetrahedral_number(2), 4) # Small value)

    def test_case_4(self):
        self.assertEqual(tetrahedral_number(3), 10) # Small value)

    def test_case_5(self):
        self.assertEqual(tetrahedral_number(4), 20) # Small value)

    def test_case_6(self):
        self.assertEqual(tetrahedral_number(10), 220) # Medium value)

    def test_case_7(self):
        self.assertEqual(tetrahedral_number(100), 171700) # Large value)

    def test_case_8(self):
        self.assertEqual(tetrahedral_number(-5), -35) # Negative value)

