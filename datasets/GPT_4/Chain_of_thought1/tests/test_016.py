import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_016 import *

class TestVersion(unittest.TestCase):
    def test_normal_case(self): result = subject_marks({'Math': 80, 'English': 70, 'Science': 90}); self.assertEqual(list(result.items()), [('English', 70), ('Math', 80), ('Science', 90)])

    def test_duplicate_marks(self): result = subject_marks({'Math': 80, 'English': 80, 'Science': 70}); self.assertEqual(list(result.items()), [('Science', 70), ('Math', 80), ('English', 80)])

    def test_already_sorted(self): result = subject_marks({'English': 60, 'Math': 70, 'Science': 80}); self.assertEqual(list(result.items()), [('English', 60), ('Math', 70), ('Science', 80)])

    def test_reverse_sorted(self): result = subject_marks({'Science': 90, 'Math': 70, 'English': 60}); self.assertEqual(list(result.items()), [('English', 60), ('Math', 70), ('Science', 90)])

    def test_empty_dict(self): self.assertEqual(subject_marks({}), {})

    def test_float_values(self): result = subject_marks({'Math': 75.5, 'English': 60.0, 'Science': 88.8}); self.assertEqual(list(result.items()), [('English', 60.0), ('Math', 75.5), ('Science', 88.8)])

    def test_negative_marks(self): result = subject_marks({'Math': -10, 'English': 0, 'Science': 10}); self.assertEqual(list(result.items()), [('Math', -10), ('English', 0), ('Science', 10)])

    def test_large_dictionary(self): d = {f'Sub{i}': i for i in range(100, 0, -1)}; sorted_keys = [f'Sub{i}' for i in range(1, 101)]; result = subject_marks(d); self.assertEqual(list(result.keys()), sorted_keys)

