import unittest
from datasets.GPT_4.Few_shot.programs.program_079 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(circle_circumference(1), 6.283) # Radius 1)

    def test_case_2(self):
        self.assertEqual(circle_circumference(0), 0) # Radius 0)

    def test_case_3(self):
        self.assertEqual(circle_circumference(2), 12.566) # Radius 2)

    def test_case_4(self):
        self.assertEqual(circle_circumference(10), 62.83) # Larger radius)

    def test_case_5(self):
        self.assertEqual(circle_circumference(0.5), 3.1415) # Small radius)

    def test_case_6(self):
        try:
            circle_circumference(-1)   # Negative radius
        except ValueError:
            print("Passed: ValueError for negative radius.")

    def test_case_7(self):
        self.assertEqual(circle_circumference(100), 628.3) # Very large radius)

    def test_case_8(self):
        self.assertEqual(circle_circumference(3.1415), 19.73930775) # Floating point radius)

