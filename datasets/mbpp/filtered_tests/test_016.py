import unittest
from datasets.mbpp.programs.program_016 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
        subject_marks([
        ('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)
        ]),
        [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
        )

    def test_case_2(self):
        self.assertEqual(
        subject_marks([
        ('Telugu', 49), ('Hindhi', 54), ('Social', 33)
        ]),
        [('Social', 33), ('Telugu', 49), ('Hindhi', 54)]
        )

    def test_case_3(self):
        self.assertEqual(
        subject_marks([
        ('Physics', 96), ('Chemistry', 97), ('Biology', 45)
        ]),
        [('Biology', 45), ('Physics', 96), ('Chemistry', 97)]
        )

