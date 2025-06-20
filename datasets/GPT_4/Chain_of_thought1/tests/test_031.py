import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_031 import *

class TestVersion(unittest.TestCase):
    def test_all_uppercase(self): self.assertEqual(get_Char('ABC'), ord('A') + ord('B') + ord('C'))

    def test_mixed_case(self): self.assertEqual(get_Char('aBcDe'), ord('B') + ord('D'))

    def test_all_lowercase(self): self.assertEqual(get_Char('abcdef'), 0)

    def test_single_uppercase(self): self.assertEqual(get_Char('Z'), ord('Z'))

    def test_special_characters(self): self.assertEqual(get_Char('@#$%^&*'), 0)

    def test_digits_and_lowercase(self): self.assertEqual(get_Char('abc123xyz'), 0)

    def test_empty_string(self): self.assertEqual(get_Char(''), 0)

    def test_unicode_uppercase(self): self.assertEqual(get_Char('ÉéA'), ord('É') + ord('A'))

