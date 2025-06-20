import unittest
from datasets.GPT_4.Few_shot2.programs.program_016 import *

class TestVersion(unittest.TestCase):
    def test_subject_marks_basic(self): import io, sys; captured = io.StringIO(); sys.stdout = captured; subject_marks({'Math': 90, 'Science': 85}); sys.stdout = sys.__stdout__; output = captured.getvalue(); self.assertIn('Math : 90', output); self.assertIn('Science : 85', output)

    def test_subject_marks_empty(self): import io, sys; captured = io.StringIO(); sys.stdout = captured; subject_marks({}); sys.stdout = sys.__stdout__; output = captured.getvalue(); self.assertEqual(output, '')

    def test_subject_marks_single_subject(self): import io, sys; captured = io.StringIO(); sys.stdout = captured; subject_marks({'History': 70}); sys.stdout = sys.__stdout__; output = captured.getvalue(); self.assertIn('History : 70', output)

    def test_subject_marks_non_string_subjects(self): import io, sys; captured = io.StringIO(); sys.stdout = captured; subject_marks({101: 88}); sys.stdout = sys.__stdout__; output = captured.getvalue(); self.assertIn('101 : 88', output)

    def test_subject_marks_zero_marks(self): import io, sys; captured = io.StringIO(); sys.stdout = captured; subject_marks({'Math': 0}); sys.stdout = sys.__stdout__; output = captured.getvalue(); self.assertIn('Math : 0', output)

