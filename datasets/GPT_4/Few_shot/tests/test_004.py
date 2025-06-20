import unittest
from datasets.GPT_4.Few_shot.programs.program_004 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(text_lowercase_underscore(""), "")

    def test_case_2(self):
        self.assertEqual(text_lowercase_underscore("Hello World"), "hello_world")

    def test_case_3(self):
        self.assertEqual(text_lowercase_underscore("  Multiple  spaces  "), "multiple_spaces")

    def test_case_4(self):
        self.assertEqual(text_lowercase_underscore("NoSpaces"), "nospaces")

    def test_case_5(self):
        self.assertEqual(text_lowercase_underscore("Special_Characters!"), "special_characters!")

    def test_case_6(self):
        self.assertEqual(text_lowercase_underscore("UPPER lower Mixed"), "upper_lower_mixed")

    def test_case_7(self):
        self.assertEqual(text_lowercase_underscore("  leading and trailing  "), "leading_and_trailing")

    def test_case_8(self):
        self.assertEqual(text_lowercase_underscore("already_lower_case"), "already_lower_case")

