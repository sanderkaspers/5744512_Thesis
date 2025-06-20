import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_006 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_dirty_chars('hello', 'world'), 'he')

    def test_no_common_characters(self):
        self.assertEqual(remove_dirty_chars('abc', 'xyz'), 'abc')

    def test_empty_first_string(self):
        self.assertEqual(remove_dirty_chars('', 'abc'), '')

    def test_empty_second_string(self):
        self.assertEqual(remove_dirty_chars('hello', ''), 'hello')

    def test_both_strings_empty(self):
        self.assertEqual(remove_dirty_chars('', ''), '')

    def test_case_sensitivity(self):
        self.assertEqual(remove_dirty_chars('Hello', 'h'), 'Hello')

    def test_repeating_characters(self):
        self.assertEqual(remove_dirty_chars('banana', 'an'), 'b')

    def test_special_characters(self):
        self.assertEqual(remove_dirty_chars('he!llo@world#', '!@#'), 'helloworld')

    def test_numeric_characters(self):
        self.assertEqual(remove_dirty_chars('123456', '345'), '126')

    def test_long_strings(self):
        self.assertEqual(remove_dirty_chars('a' * 1000 + 'b' * 1000, 'b'), 'a' * 1000)

    def test_unicode_characters(self):
        self.assertEqual(remove_dirty_chars('héllò', 'ò'), 'héll')

    def test_mixed_content(self):
        self.assertEqual(remove_dirty_chars('abc123!@#', '23!'), 'abc1@#')

    def test_non_ascii_in_second_string(self):
        self.assertEqual(remove_dirty_chars('hello', 'é'), 'hello')

    def test_string_with_spaces(self):
        self.assertEqual(remove_dirty_chars('hello world', ' '), 'helloworld')

    def test_all_characters_removed(self):
        self.assertEqual(remove_dirty_chars('abc', 'abc'), '')

