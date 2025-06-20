import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_004 import *

class TestVersion(unittest.TestCase):
    def test_mixed_case(self): self.assertEqual(text_lowercase_underscore("HelloWorld"), "helloworld")

    def test_with_punctuation(self): self.assertEqual(text_lowercase_underscore("Hello, World!"), "hello_world")

    def test_with_spaces(self): self.assertEqual(text_lowercase_underscore("This is a test"), "this_is_a_test")

    def test_letters_and_digits(self): self.assertEqual(text_lowercase_underscore("File123Test"), "file123test")

    def test_with_underscores(self): self.assertEqual(text_lowercase_underscore("user_name_1"), "user_name_1")

    def test_empty_string(self): self.assertEqual(text_lowercase_underscore(""), "")

    def test_symbols_only(self): self.assertEqual(text_lowercase_underscore("$$$%%%"), "_")

    def test_consecutive_symbols(self): self.assertEqual(text_lowercase_underscore("a!!b@@c"), "a_b_c")

    def test_uppercase_only(self): self.assertEqual(text_lowercase_underscore("ALLCAPS"), "allcaps")

    def test_unicode_input(self): self.assertEqual(text_lowercase_underscore("café & crème"), "café_crème")

