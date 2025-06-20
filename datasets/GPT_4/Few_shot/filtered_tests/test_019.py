import unittest
from datasets.GPT_4.Few_shot.programs.program_019 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(bell_number(0), 1) # Edge case for zero)

    def test_case_2(self):
        self.assertEqual(bell_number(1), 1) # Small value)

    def test_case_3(self):
        self.assertEqual(bell_number(2), 2) # Small value)

    def test_case_4(self):
        self.assertEqual(bell_number(3), 5) # Small value)

    def test_case_5(self):
        self.assertEqual(bell_number(4), 15) # Small value)

    def test_case_6(self):
        self.assertEqual(bell_number(5), 52) # Small value)

    def test_case_7(self):
        self.assertEqual(bell_number(10), 115975) # Medium value)

    def test_case_8(self):
        self.assertEqual(bell_number(20), 51724158235372) # Large value)

