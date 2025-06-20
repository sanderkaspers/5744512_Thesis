import unittest
from datasets.o3.programs.program_016 import *

class TestVersion(unittest.TestCase):
    def test_subject_marks_unsorted(self):
        data = [('Maths', 97), ('English', 88), ('Science', 90)]
        expected = [('English', 88), ('Science', 90), ('Maths', 97)]
        self.assertEqual(subject_marks(data.copy()), expected)

    def test_subject_marks_already_sorted(self):
        data = [('English', 70), ('Maths', 80)]
        expected = [('English', 70), ('Maths', 80)]
        self.assertEqual(subject_marks(data.copy()), expected)

    def test_subject_marks_duplicate_scores(self):
        data = [('Eng', 80), ('Sci', 90), ('Math', 80)]
        expected = [('Eng', 80), ('Math', 80), ('Sci', 90)]
        self.assertEqual(subject_marks(data.copy()), expected)

    def test_subject_marks_single_entry(self):
        data = [('Geography', 75)]
        self.assertEqual(subject_marks(data.copy()), data)

    def test_subject_marks_empty(self):
        self.assertEqual(subject_marks([]), [])

