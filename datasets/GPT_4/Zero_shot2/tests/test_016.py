import unittest
from datasets.GPT_4.Zero_shot2.programs.program_016 import *

class TestVersion(unittest.TestCase):
    def test_marks_1(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        subject_marks({'Math': 90})
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), 'Math : 90\n')

    def test_marks_2(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        subject_marks({'Math': 90, 'Science': 80})
        sys.stdout = sys.__stdout__
        lines = captured_output.getvalue().strip().split('\n')
        self.assertIn('Math : 90', lines)
        self.assertIn('Science : 80', lines)

    def test_marks_3(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        subject_marks({101: 'A', 102: 'B'})
        sys.stdout = sys.__stdout__
        lines = captured_output.getvalue().strip().split('\n')
        self.assertIn('101 : A', lines)
        self.assertIn('102 : B', lines)

    def test_marks_4(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        subject_marks({})
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), '')

    def test_marks_5(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        subject_marks({'Eng&Lit': "@95!"})
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), 'Eng&Lit : @95!\n')

