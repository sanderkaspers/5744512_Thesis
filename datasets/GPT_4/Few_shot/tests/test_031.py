import unittest
from datasets.GPT_4.Few_shot.programs.program_031 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(get_Char("ABC"), 198) # ASCII values: 65 + 66 + 67)

    def test_case_2(self):
        self.assertEqual(get_Char(""), 0) # Empty string)

    def test_case_3(self):
        self.assertEqual(get_Char("a"), 97) # Single character)

    def test_case_4(self):
        self.assertEqual(get_Char("Hello!"), 500) # String with special character)

    def test_case_5(self):
        self.assertEqual(get_Char(" "), 32) # Single space)

    def test_case_6(self):
        self.assertEqual(get_Char("\n"), 10) # Newline character)

    def test_case_7(self):
        self.assertEqual(get_Char("12345"), 255) # String with digits)

    def test_case_8(self):
        self.assertEqual(get_Char("~!@) #$%^&*()_+"), 1230 ) # String with various special characters)

