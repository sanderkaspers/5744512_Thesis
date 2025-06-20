import unittest
from datasets.GPT_4.Zero_shot2.programs.program_001 import *

class TestVersion(unittest.TestCase):
    def test_remove_occ_1(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        remove_Occ("hello world", "l")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "heo word")

    def test_remove_occ_2(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        remove_Occ("abcdef", "z")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "abcdef")

    def test_remove_occ_3(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        remove_Occ("aaaaa", "a")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "")

    def test_remove_occ_4(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        remove_Occ("", "a")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "")

    def test_remove_occ_5(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        remove_Occ("a b c", " ")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "abc")

    def test_remove_occ_6(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        remove_Occ("!@#$$%^", "$")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "!@#%^")

