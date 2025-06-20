import unittest
from datasets.GPT_4.Few_shot1.programs.program_013 import *

class TestVersion(unittest.TestCase):
    def test_count_characters_empty_string(self): self.assertEqual(count_characters(""), {})

    def test_count_characters_single_char(self): self.assertEqual(count_characters("a"), {"a": 1})

    def test_count_characters_repeated_char(self): self.assertEqual(count_characters("aaa"), {"a": 3})

    def test_count_characters_mixed_case(self): self.assertEqual(count_characters("aAa"), {"a": 2, "A": 1})

    def test_count_characters_with_digits(self): self.assertEqual(count_characters("a1a2"), {"a": 2, "1": 1, "2": 1})

    def test_count_characters_with_punctuation(self): self.assertEqual(count_characters("a!a."), {"a": 2, "!": 1, ".": 1})

    def test_count_characters_with_whitespace(self): self.assertEqual(count_characters("a a"), {"a": 2, " ": 1})

    def test_count_characters_unicode(self): self.assertEqual(count_characters("你好你"), {"你": 2, "好": 1})

    def test_count_characters_long_string(self): self.assertEqual(count_characters("abc" * 1000), {"a": 1000, "b": 1000, "c": 1000})

