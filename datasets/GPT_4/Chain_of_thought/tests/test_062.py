import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_062 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(string_to_list('hello world this is a test'), ['hello', 'world', 'this', 'is', 'a', 'test'])

    def test_consecutive_spaces(self):
        self.assertEqual(string_to_list('hello  world  test'), ['hello', '', 'world', '', 'test'])

    def test_leading_trailing_spaces(self):
        self.assertEqual(string_to_list('  hello world  '), ['', '', 'hello', 'world', '', ''])

    def test_empty_string(self):
        self.assertEqual(string_to_list(''), [''])

    def test_no_spaces(self):
        self.assertEqual(string_to_list('helloworld'), ['helloworld'])

    def test_special_characters(self):
        self.assertEqual(string_to_list('hello@world#test!'), ['hello@world#test!'])

    def test_numbers_in_string(self):
        self.assertEqual(string_to_list('123 456 789'), ['123', '456', '789'])

    def test_mixed_case_letters(self):
        self.assertEqual(string_to_list('Hello World This Is A Test'), ['Hello', 'World', 'This', 'Is', 'A', 'Test'])

    def test_tabs_or_newlines(self):
        self.assertEqual(string_to_list('hello\tworld\nthis is a test'), ['hello\tworld\nthis', 'is', 'a', 'test'])

    def test_very_long_string(self):
        long_string = 'word ' * 1000
        self.assertEqual(string_to_list(long_string), ['word'] * 1000)

