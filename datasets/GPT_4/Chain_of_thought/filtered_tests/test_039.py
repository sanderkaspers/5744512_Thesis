import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_039 import *

class TestVersion(unittest.TestCase):
    def test_typical_case_present(self):
        self.assertTrue(find_substring(['apple', 'banana', 'cherry'], 'ana'))

    def test_substring_not_present(self):
        self.assertFalse(find_substring(['apple', 'banana', 'cherry'], 'grape'))

    def test_empty_substring(self):
        self.assertTrue(find_substring(['apple', 'banana', 'cherry'], ''))

    def test_empty_list(self):
        self.assertFalse(find_substring([], 'ana'))

    def test_empty_strings_in_list(self):
        self.assertFalse(find_substring(['', '', ''], 'ana'))

    def test_substring_at_beginning(self):
        self.assertTrue(find_substring(['apple', 'banana', 'cherry'], 'app'))

    def test_substring_at_end(self):
        self.assertTrue(find_substring(['apple', 'banana', 'cherry'], 'erry'))

    def test_substring_in_middle(self):
        self.assertTrue(find_substring(['apple', 'banana', 'cherry'], 'nan'))

    def test_case_sensitivity(self):
        self.assertFalse(find_substring(['apple', 'banana', 'cherry'], 'Ana'))

    def test_special_characters(self):
        self.assertTrue(find_substring(['apple$', 'banana#', 'cherry@'], '$'))

