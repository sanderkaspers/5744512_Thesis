import unittest
from datasets.GPT_4.Few_shot1.programs.program_016 import *

class TestVersion(unittest.TestCase):
    def test_subject_marks_empty_dict(self): self.assertEqual(subject_marks({}), [])

    def test_subject_marks_single_pair(self): self.assertEqual(subject_marks({"Math": 95}), [("Math", 95)])

    def test_subject_marks_sorted_order(self): self.assertEqual(subject_marks({"Math": 95, "English": 90, "Science": 85}), [("Math", 95), ("English", 90), ("Science", 85)])

    def test_subject_marks_unsorted_input(self): self.assertEqual(subject_marks({"Science": 85, "Math": 95, "English": 90}), [("Math", 95), ("English", 90), ("Science", 85)])

    def test_subject_marks_same_scores(self): self.assertEqual(subject_marks({"Math": 90, "English": 90, "Science": 90}), [("Math", 90), ("English", 90), ("Science", 90)])

    def test_subject_marks_with_zero(self): self.assertEqual(subject_marks({"Math": 0, "English": 90, "Science": 45}), [("English", 90), ("Science", 45), ("Math", 0)])

    def test_subject_marks_negative_scores(self): self.assertEqual(subject_marks({"Math": -10, "English": 0, "Science": -5}), [("English", 0), ("Science", -5), ("Math", -10)])

    def test_subject_marks_large_values(self): self.assertEqual(subject_marks({"Math": 100000, "English": 99999}), [("Math", 100000), ("English", 99999)])

    def test_subject_marks_duplicate_subjects(self): d = {"Math": 100, "Math": 50}; self.assertEqual(subject_marks(d), [("Math", 50)])

