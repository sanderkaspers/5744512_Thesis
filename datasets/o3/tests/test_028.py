import unittest
from datasets.o3.programs.program_028 import *

class TestVersion(unittest.TestCase):
    def test_simple_sentence(self):
        self.assertEqual(word_len("Hello world"), 2)

    def test_leading_trailing_spaces(self):
        self.assertEqual(word_len("   hello   "), 1)

    def test_multiple_spaces_between(self):
        self.assertEqual(word_len("a  b   c"), 3)

    def test_empty_string(self):
        self.assertEqual(word_len(""), 0)

    def test_tabs_newlines_present(self):
        self.assertEqual(word_len("a\n b\tc"), 2)

