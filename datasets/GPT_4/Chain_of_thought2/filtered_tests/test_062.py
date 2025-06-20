import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_062 import *

class TestVersion(unittest.TestCase):
    def test_simple_split(self): self.assertEqual(string_to_list('hello world'), ['hello', 'world'])

    def test_empty_string(self): self.assertEqual(string_to_list(''), [''])

    def test_leading_space(self): self.assertEqual(string_to_list(' hello'), ['', 'hello'])

    def test_trailing_space(self): self.assertEqual(string_to_list('world '), ['world', ''])

    def test_leading_and_trailing_spaces(self): self.assertEqual(string_to_list('  hi  '), ['', '', 'hi', '', ''])

    def test_multiple_spaces_between_words(self): self.assertEqual(string_to_list('a  b   c'), ['a', '', 'b', '', '', 'c'])

    def test_single_word(self): self.assertEqual(string_to_list('test'), ['test'])

    def test_only_spaces(self): self.assertEqual(string_to_list('     '), ['', '', '', '', '', ''])

    def test_with_tabs_and_newlines(self): self.assertEqual(string_to_list('a\tb\nc'), ['a\tb\nc'])

    def test_non_ascii_characters(self): self.assertEqual(string_to_list('café au lait'), ['café', 'au', 'lait'])

    def test_long_string_with_spaces(self): self.assertEqual(string_to_list('a ' * 10), ['a'] * 10 + [''])

