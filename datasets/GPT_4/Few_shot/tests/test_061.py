import unittest
from datasets.GPT_4.Few_shot.programs.program_061 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(list_to_float(["1.1", "2.2", "3.3"]), [1.1, 2.2, 3.3]) # All valid numeric strings)

    def test_case_2(self):
        try:
            list_to_float(["1.1", "abc", "3.3"])   # Mixed valid and invalid strings
        except ValueError:
            print("Passed: ValueError for invalid string.")

    def test_case_3(self):
        self.assertEqual(list_to_float([]), []) # Empty list)

    def test_case_4(self):
        try:
            list_to_float(["abc", "def"])   # All invalid strings
        except ValueError:
            print("Passed: ValueError for invalid strings.")

    def test_case_5(self):
        self.assertEqual(list_to_float(["0.0", "1.0", "2.0"]), [0.0, 1.0, 2.0]) # Strings with zeros)

    def test_case_6(self):
        self.assertEqual(list_to_float(["-1.1", "-2.2", "-3.3"]), [-1.1, -2.2, -3.3]) # Negative numbers as strings)

    def test_case_7(self):
        try:
            list_to_float(["1.1", "2.2", None])   # None in the list
        except TypeError:
            print("Passed: TypeError for None value.")

    def test_case_8(self):
        self.assertEqual(list_to_float(["100", "200", "300"]), [100.0, 200.0, 300.0]) # Integer-like strings)

