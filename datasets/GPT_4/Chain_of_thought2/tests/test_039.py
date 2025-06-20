import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_039 import *

class TestVersion(unittest.TestCase):
    def test_exact_match_in_list(self): self.assertTrue(find_substring(['apple', 'banana', 'cherry'], 'banana'))

    def test_partial_match_in_list(self): self.assertTrue(find_substring(['carpet', 'mat', 'floor'], 'pet'))

    def test_full_string_is_substring(self): self.assertTrue(find_substring(['antelope', 'bear', 'cat'], 'lope'))

    def test_multiple_occurrences(self): self.assertTrue(find_substring(['abc', 'defabc', 'xyzabc'], 'abc'))

    def test_no_occurrence(self): self.assertFalse(find_substring(['one', 'two', 'three'], 'four'))

    def test_empty_list(self): self.assertFalse(find_substring([], 'any'))

    def test_empty_substring(self): self.assertTrue(find_substring(['a', 'b'], ''))

    def test_case_sensitive(self): self.assertFalse(find_substring(['Hello', 'World'], 'hello'))

    def test_list_with_empty_strings(self): self.assertFalse(find_substring(['', '', ''], 'non'))

    def test_substring_longer_than_elements(self): self.assertFalse(find_substring(['hi', 'ok', 'yo'], 'hello'))

