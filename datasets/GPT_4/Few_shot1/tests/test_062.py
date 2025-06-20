import unittest
from datasets.GPT_4.Few_shot1.programs.program_062 import *

class TestVersion(unittest.TestCase):
    def test_string_to_list_basic(self): self.assertEqual(string_to_list("hello world"), ["hello", "world"])

    def test_string_to_list_multiple_spaces(self): self.assertEqual(string_to_list("a  b   c"), ["a", "", "b", "", "", "c"])

    def test_string_to_list_empty(self): self.assertEqual(string_to_list(""), [""])

    def test_string_to_list_single_word(self): self.assertEqual(string_to_list("python"), ["python"])

    def test_string_to_list_trailing_space(self): self.assertEqual(string_to_list("end "), ["end", ""])

    def test_string_to_list_leading_space(self): self.assertEqual(string_to_list(" start"), ["", "start"])

    def test_string_to_list_only_spaces(self): self.assertEqual(string_to_list("   "), ["", "", "", ""])

