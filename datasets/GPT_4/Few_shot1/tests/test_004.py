import unittest
from datasets.GPT_4.Few_shot1.programs.program_004 import *

class TestVersion(unittest.TestCase):
    def test_text_lowercase_underscore_all_lowercase(self): self.assertEqual(text_lowercase_underscore("hello"), "hello")

    def test_text_lowercase_underscore_all_uppercase(self): self.assertEqual(text_lowercase_underscore("HELLO"), "hello")

    def test_text_lowercase_underscore_mixed_case(self): self.assertEqual(text_lowercase_underscore("HeLLo"), "hello")

    def test_text_lowercase_underscore_with_spaces(self): self.assertEqual(text_lowercase_underscore("Hello World"), "hello_world")

    def test_text_lowercase_underscore_with_punctuation(self): self.assertEqual(text_lowercase_underscore("Hello, World!"), "hello_world_")

    def test_text_lowercase_underscore_digits_and_letters(self): self.assertEqual(text_lowercase_underscore("abc123"), "abc123")

    def test_text_lowercase_underscore_special_chars_only(self): self.assertEqual(text_lowercase_underscore("@#$%^"), "_")

    def test_text_lowercase_underscore_underscore_chars(self): self.assertEqual(text_lowercase_underscore("hello_world"), "hello_world")

    def test_text_lowercase_underscore_empty_string(self): self.assertEqual(text_lowercase_underscore(""), "")

    def test_text_lowercase_underscore_multiple_specials(self): self.assertEqual(text_lowercase_underscore("Hi!! How--are_you?"), "hi_how_are_you_")

