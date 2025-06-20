import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_039 import *

class TestVersion(unittest.TestCase):
    def test_sub_in_word(self): self.assertTrue(find_substring('hello world', 'wor'))

    def test_sub_is_full_word(self): self.assertTrue(find_substring('hello world', 'world'))

    def test_not_present(self): self.assertFalse(find_substring('hello there', 'xyz'))

    def test_multiple_matches(self): self.assertTrue(find_substring('hi he hello', 'he'))

    def test_empty_main_string(self): self.assertFalse(find_substring('', 'hi'))

    def test_empty_substring(self): self.assertTrue(find_substring('hello world', ''))

    def test_space_substring(self): self.assertFalse(find_substring('hello world', ' '))

    def test_case_sensitivity(self): self.assertFalse(find_substring('Hello World', 'world'))

