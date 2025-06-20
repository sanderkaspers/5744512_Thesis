import unittest
from datasets.GPT_4.Few_shot.programs.program_034 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(centered_hexagonal_number(1), 1) # Edge case n = 1)

    def test_case_2(self):
        self.assertEqual(centered_hexagonal_number(2), 7) # Small value)

    def test_case_3(self):
        self.assertEqual(centered_hexagonal_number(3), 19) # Small value)

    def test_case_4(self):
        self.assertEqual(centered_hexagonal_number(4), 37) # Small value)

    def test_case_5(self):
        self.assertEqual(centered_hexagonal_number(10), 271) # Medium value)

    def test_case_6(self):
        self.assertEqual(centered_hexagonal_number(100), 29701) # Large value)

    def test_case_7(self):
        self.assertEqual(centered_hexagonal_number(0), 1) # Edge case n = 0)

    def test_case_8(self):
        self.assertEqual(centered_hexagonal_number(-5), 61) # Negative value (absolute value effect))

