import unittest
from datasets.GPT_4.Zero_shot1.programs.program_016 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(subject_marks([("Math", 30), ("English", 40)]), [])

    def test_2(self):
        self.assertEqual(subject_marks([("Math", 49), ("English", 50), ("Science", 51)]), [("English", 50), ("Science", 51)])

    def test_3(self):
        self.assertEqual(subject_marks([]), [])

    def test_4(self):
        self.assertEqual(subject_marks([("Math", 50)]), [("Math", 50)])

    def test_5(self):
        self.assertEqual(subject_marks([("Math", -10), ("Science", 90)]), [("Science", 90)])

    def test_6(self):
        self.assertEqual(subject_marks([("Art", 100), ("Art", 30)]), [("Art", 100)])

    def test_7(self):
        self.assertEqual(subject_marks([("Music", 49.9), ("PE", 50.0)]), [("PE", 50.0)])

