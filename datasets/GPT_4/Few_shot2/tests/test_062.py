import unittest
from datasets.GPT_4.Few_shot2.programs.program_062 import *

class TestVersion(unittest.TestCase):
    def test_string_to_list_regular(self): self.assertEqual(string_to_list('hello'), ['h', 'e', 'l', 'l', 'o'])

    def test_string_to_list_empty(self): self.assertEqual(string_to_list(''), [])

    def test_string_to_list_with_spaces(self): self.assertEqual(string_to_list('hi there'), ['h', 'i', ' ', 't', 'h', 'e', 'r', 'e'])

    def test_string_to_list_with_numbers(self): self.assertEqual(string_to_list('abc123'), ['a', 'b', 'c', '1', '2', '3'])

    def test_string_to_list_with_symbols(self): self.assertEqual(string_to_list('!@#'), ['!', '@', '#'])

    def test_string_to_list_unicode(self): self.assertEqual(string_to_list('你好'), ['你', '好'])

    def test_string_to_list_whitespace_only(self): self.assertEqual(string_to_list('   '), [' ', ' ', ' '])

    def test_string_to_list_mixed_types(self): self.assertEqual(string_to_list('a B 1!'), ['a', ' ', 'B', ' ', '1', '!'])

