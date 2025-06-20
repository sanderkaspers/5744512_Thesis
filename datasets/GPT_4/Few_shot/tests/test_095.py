import unittest
from datasets.GPT_4.Few_shot.programs.program_095 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(perimeter_pentagon(1), 5) # Small side length)

    def test_case_2(self):
        self.assertEqual(perimeter_pentagon(10), 50) # Larger side length)

    def test_case_3(self):
        self.assertEqual(perimeter_pentagon(0), 0) # Edge case with side length 0)

    def test_case_4(self):
        try:
            perimeter_pentagon(-5)   # Negative side length
        except ValueError:
            print("Passed: ValueError for negative side length.")

    def test_case_5(self):
        self.assertEqual(perimeter_pentagon(100), 500) # Very large side length)

    def test_case_6(self):
        self.assertEqual(perimeter_pentagon(0.5), 2.5) # Small positive side length)

    def test_case_7(self):
        self.assertEqual(perimeter_pentagon(2), 10) # Small positive side length)

    def test_case_8(self):
        self.assertEqual(perimeter_pentagon(7.5), 37.5) # Floating point side length)

