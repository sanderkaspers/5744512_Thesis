import unittest
from datasets.GPT_4.Few_shot2.programs.program_038 import *

class TestVersion(unittest.TestCase):
    def test_len_log_single_element(self): self.assertEqual(len_log(['one']), 'one')

    def test_len_log_all_equal_length(self): self.assertEqual(len_log(['a', 'b', 'c']), 'a')

    def test_len_log_varying_lengths(self): self.assertEqual(len_log(['cat', 'horse', 'cow']), 'horse')

    def test_len_log_with_spaces(self): self.assertEqual(len_log(['hi', 'hello world', 'hey']), 'hello world')

    def test_len_log_empty_string_inside(self): self.assertEqual(len_log(['', 'a', 'ab']), 'ab')

    def test_len_log_only_empty_string(self): self.assertEqual(len_log(['']), '')

    def test_len_log_all_empty_strings(self): self.assertEqual(len_log(['', '', '']), '')

    def test_len_log_numbers_as_strings(self): self.assertEqual(len_log(['1', '22', '333']), '333')

    def test_len_log_special_characters(self): self.assertEqual(len_log(['@', '#$%', '&*']), '#$%')

    def test_len_log_unicode_characters(self): self.assertEqual(len_log(['ñ', '你好', '😊😊😊']), '😊😊😊')

