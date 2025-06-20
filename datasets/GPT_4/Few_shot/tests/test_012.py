import unittest
from datasets.GPT_4.Few_shot.programs.program_012 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_octagonal(1), 1) # Smallest positive integer)

    def test_case_2(self):
        self.assertEqual(is_octagonal(0), 0) # Edge case zero)

    def test_case_3(self):
        self.assertEqual(is_octagonal(2), 10) # Small positive integer)

    def test_case_4(self):
        self.assertEqual(is_octagonal(-1), 5) # Negative number)

    def test_case_5(self):
        self.assertEqual(is_octagonal(100), 29800) # Large number)

    def test_case_6(self):
        self.assertEqual(is_octagonal(-100), 30200) # Large negative number)

    def test_case_7(self):
        self.assertEqual(is_octagonal(10), 280) # Medium positive number)

    def test_case_8(self):
        self.assertEqual(is_octagonal(5), 55) # Small positive number)

