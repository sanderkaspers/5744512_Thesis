import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_062 import *

class TestVersion(unittest.TestCase):
    def test_normal_string(self): self.assertEqual(string_to_list('hello'), ['h', 'e', 'l', 'l', 'o'])

    def test_string_with_spaces(self): self.assertEqual(string_to_list('a b c'), ['a', ' ', 'b', ' ', 'c'])

    def test_empty_string(self): self.assertEqual(string_to_list(''), [])

    def test_punctuation(self): self.assertEqual(string_to_list('a,b.c!'), ['a', ',', 'b', '.', 'c', '!'])

    def test_numeric_string(self): self.assertEqual(string_to_list('12345'), ['1', '2', '3', '4', '5'])

    def test_unicode(self): self.assertEqual(string_to_list('你好'), ['你', '好'])

    def test_list_input(self): self.assertEqual(string_to_list(['a', 'b']), ['[', "'", 'a', "'", ',', ' ', "'", 'b', "'", ']'])

    def test_escape_characters(self): self.assertEqual(string_to_list('\n\t'), ['\n', '\t'])

    def test_long_string(self): s = 'a' * 1000; self.assertEqual(string_to_list(s), ['a'] * 1000)

