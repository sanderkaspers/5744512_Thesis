import unittest
from datasets.mbpp.programs.program_004 import *

class TestVersion(unittest.TestCase):
    def test_text_lowercase_underscore_with_aab_cbbbc_expect__True_(self):
        self.assertEqual(text_lowercase_underscore("aab_cbbbc"), (True))

    def test_text_lowercase_underscore_with_aab_Abbbc_expect__False_(self):
        self.assertEqual(text_lowercase_underscore("aab_Abbbc"), (False))

    def test_text_lowercase_underscore_with_Aaab_abbbc_expect__False_(self):
        self.assertEqual(text_lowercase_underscore("Aaab_abbbc"), (False))

