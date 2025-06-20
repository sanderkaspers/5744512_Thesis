import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_004 import *

class TestVersion(unittest.TestCase):
    def test_basic_sentence(self): self.assertEqual(text_lowercase_underscore('Hello World'), 'hello_world')

    def test_multiple_spaces(self): self.assertEqual(text_lowercase_underscore('Hello   World'), 'hello_world')

    def test_mixed_case(self): self.assertEqual(text_lowercase_underscore('HeLLo WoRLd'), 'hello_world')

    def test_already_lowercase(self): self.assertEqual(text_lowercase_underscore('hello world'), 'hello_world')

    def test_tabs_and_newlines(self): self.assertEqual(text_lowercase_underscore('Hello\tWorld\nPython'), 'hello_world_python')

    def test_leading_trailing_spaces(self): self.assertEqual(text_lowercase_underscore('   Hello World   '), 'hello_world')

    def test_empty_string(self): self.assertEqual(text_lowercase_underscore(''), '')

    def test_only_whitespace(self): self.assertEqual(text_lowercase_underscore('   \t \n  '), '_')

    def test_special_chars_digits(self): self.assertEqual(text_lowercase_underscore('HeLLo 123! @World'), 'hello_123!_@world')

    def test_no_whitespace(self): self.assertEqual(text_lowercase_underscore('NoSpacesHere'), 'nospaceshere')

    def test_unicode_text(self): self.assertEqual(text_lowercase_underscore('Привет Мир'), 'привет_мир')

