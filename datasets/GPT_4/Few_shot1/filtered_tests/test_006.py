import unittest
from datasets.GPT_4.Few_shot1.programs.program_006 import *

class TestVersion(unittest.TestCase):
    def test_str_to_list_basic_string(self): self.assertEqual(str_to_list("hello"), ['h', 'e', 'l', 'l', 'o'])

    def test_str_to_list_empty_string(self): self.assertEqual(str_to_list(""), [])

    def test_str_to_list_spaces(self): self.assertEqual(str_to_list("a b"), ['a', ' ', 'b'])

    def test_str_to_list_special_characters(self): self.assertEqual(str_to_list("!@#"), ['!', '@', '#'])

    def test_str_to_list_unicode_characters(self): self.assertEqual(str_to_list("你好"), ['你', '好'])

    def test_str_to_list_numbers(self): self.assertEqual(str_to_list("12345"), ['1', '2', '3', '4', '5'])

    def test_str_to_list_mixed_string(self): self.assertEqual(str_to_list("A1! "), ['A', '1', '!', ' '])

    def test_str_to_list_newlines_and_tabs(self): self.assertEqual(str_to_list("a\nb\tc"), ['a', '\n', 'b', '\t', 'c'])

    def test_str_to_list_long_string(self): long_str = "a" * 1000; self.assertEqual(str_to_list(long_str), ['a'] * 1000)

