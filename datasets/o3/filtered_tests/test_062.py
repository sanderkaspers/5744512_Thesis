import unittest
from datasets.o3.programs.program_062 import *

class TestVersion(unittest.TestCase):
    def test_regular_sentence(self):
        self.assertEqual(string_to_list("hello world"), ["hello","world"])

    def test_multiple_spaces(self):
        self.assertEqual(string_to_list("a  b"), ["a","","b"])

    def test_leading_trailing_spaces(self):
        self.assertEqual(string_to_list("  lead space"), ["","","lead","space"])

    def test_empty_string(self):
        self.assertEqual(string_to_list(""), [""])

    def test_special_characters(self):
        self.assertEqual(string_to_list("hello, world!"), ["hello,","world!"])

