import unittest
from datasets.GPT_4.Few_shot1.programs.program_039 import *

class TestVersion(unittest.TestCase):
    def test_find_substring_present(self): self.assertEqual(find_substring("hello world", "world"), 6)

    def test_find_substring_start(self): self.assertEqual(find_substring("hello world", "hello"), 0)

    def test_find_substring_end(self): self.assertEqual(find_substring("hello world", "d"), 10)

    def test_find_substring_not_found(self): self.assertEqual(find_substring("hello world", "python"), -1)

    def test_find_substring_empty_sub(self): self.assertEqual(find_substring("hello", ""), 0)

    def test_find_substring_empty_str1(self): self.assertEqual(find_substring("", "hello"), -1)

    def test_find_substring_both_empty(self): self.assertEqual(find_substring("", ""), 0)

