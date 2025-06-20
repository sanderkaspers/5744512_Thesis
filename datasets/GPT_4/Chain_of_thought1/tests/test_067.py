import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_067 import *

class TestVersion(unittest.TestCase):
    def test_empty_string(self): self.assertEqual(find_length(''), 0)

    def test_single_char(self): self.assertEqual(find_length('a'), 1)

    def test_typical_word(self): self.assertEqual(find_length('hello'), 5)

    def test_string_with_spaces(self): self.assertEqual(find_length('a b c'), 5)

    def test_special_characters(self): self.assertEqual(find_length('!@#$%'), 5)

    def test_unicode(self): self.assertEqual(find_length('你好'), 2)

    def test_long_string(self): self.assertEqual(find_length('a' * 1000), 1000)

    def test_multiline(self): self.assertEqual(find_length('a\nb\nc'), 5)

    def test_emoji(self): self.assertEqual(find_length('🙂🙃'), 2)

