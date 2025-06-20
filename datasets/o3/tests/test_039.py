import unittest
from datasets.o3.programs.program_039 import *

class TestVersion(unittest.TestCase):
    def test_substring_present(self):
        self.assertTrue(find_substring(["hello","world"], "wor"))

    def test_multiple_occurrences(self):
        self.assertTrue(find_substring(["aaaa","bbbbaaaa","cccc"], "aaa"))

    def test_substring_absent(self):
        self.assertFalse(find_substring(["foo","bar"], "baz"))

    def test_empty_substring(self):
        self.assertTrue(find_substring(["foo","bar"], ""))

    def test_empty_list(self):
        self.assertFalse(find_substring([], "anything"))

    def test_case_sensitivity(self):
        self.assertFalse(find_substring(["Hello"], "hello"))

    def test_full_match(self):
        self.assertTrue(find_substring(["exact"], "exact"))

