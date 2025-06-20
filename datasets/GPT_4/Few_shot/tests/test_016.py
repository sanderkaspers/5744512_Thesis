import unittest
from datasets.GPT_4.Few_shot.programs.program_016 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(subject_marks([]), {}) # Empty list)

    def test_case_2(self):
        self.assertEqual(subject_marks([("Math", 95)]), {"Math": 95}) # Single subject)

    def test_case_3(self):
        self.assertEqual(subject_marks([("Math", 95), ("Math", 85), ("Science", 90)]), {"Math": 180, "Science": 90}) # Repeated subject)

    def test_case_4(self):
        self.assertEqual(subject_marks([("Math", 95), ("Science", 90), ("English", 85)]), {"Math": 95, "Science": 90, "English": 85}) # Unique subjects)

    def test_case_5(self):
        self.assertEqual(subject_marks([("Math", -10), ("Math", 20)]), {"Math": 10}) # Negative marks)

    def test_case_6(self):
        self.assertEqual(subject_marks([("History", 50), ("History", 50), ("Math", 100)]), {"History": 100, "Math": 100}) # Multiple entries)

