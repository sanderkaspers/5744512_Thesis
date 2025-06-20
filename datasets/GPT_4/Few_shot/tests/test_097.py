import unittest
from datasets.GPT_4.Few_shot.programs.program_097 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(check_type((1, 2, 3)), True) # All integers)

    def test_case_2(self):
        self.assertEqual(check_type((1, "a", 3.0)), False) # Mixed types)

    def test_case_3(self):
        self.assertEqual(check_type(()), True) # Empty tuple)

    def test_case_4(self):
        self.assertEqual(check_type(("a", "b", "c")), True) # All strings)

    def test_case_5(self):
        self.assertEqual(check_type((True, False, True)), True) # All booleans)

    def test_case_6(self):
        self.assertEqual(check_type((1,)), True) # Single element)

    def test_case_7(self):
        self.assertEqual(check_type((1.0, 2.0, 3.0)), True) # All floats)

    def test_case_8(self):
        self.assertEqual(check_type((None, None)), True) # All None)

