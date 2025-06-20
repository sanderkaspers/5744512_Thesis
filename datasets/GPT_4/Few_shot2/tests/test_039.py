import unittest
from datasets.GPT_4.Few_shot2.programs.program_039 import *

class TestVersion(unittest.TestCase):
    def test_find_substring_common_chars(self): self.assertTrue(find_substring('hello', 'world'))

    def test_find_substring_no_common_chars(self): self.assertFalse(find_substring('abc', 'xyz'))

    def test_find_substring_full_match(self): self.assertTrue(find_substring('hello', 'hello'))

    def test_find_substring_partial_char_match(self): self.assertTrue(find_substring('python', 'th'))

    def test_find_substring_case_sensitive(self): self.assertFalse(find_substring('Hello', 'hello'))

    def test_find_substring_empty_str1(self): self.assertFalse(find_substring('', 'anything'))

    def test_find_substring_empty_substr(self): self.assertFalse(find_substring('something', ''))

    def test_find_substring_both_empty(self): self.assertFalse(find_substring('', ''))

    def test_find_substring_numeric(self): self.assertTrue(find_substring('123', '345'))

    def test_find_substring_special_characters(self): self.assertTrue(find_substring('!@#', '@$%'))

