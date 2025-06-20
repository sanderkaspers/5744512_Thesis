import unittest
from datasets.GPT_4.Few_shot2.programs.program_006 import *

class TestVersion(unittest.TestCase):
    def test_str_to_list_basic_string(self): result = str_to_list('abc'); expected = [0]*256; expected[ord('a')] = 1; expected[ord('b')] = 1; expected[ord('c')] = 1; self.assertEqual(result, expected)

    def test_str_to_list_repeated_chars(self): result = str_to_list('aabbcc'); expected = [0]*256; expected[ord('a')] = 2; expected[ord('b')] = 2; expected[ord('c')] = 2; self.assertEqual(result, expected)

    def test_str_to_list_with_digits(self): result = str_to_list('123'); expected = [0]*256; expected[ord('1')] = 1; expected[ord('2')] = 1; expected[ord('3')] = 1; self.assertEqual(result, expected)

    def test_str_to_list_empty_string(self): result = str_to_list(''); expected = [0]*256; self.assertEqual(result, expected)

    def test_str_to_list_special_characters(self): result = str_to_list('!@#'); expected = [0]*256; expected[ord('!')] = 1; expected[ord('@')] = 1; expected[ord('#')] = 1; self.assertEqual(result, expected)

    def test_str_to_list_all_same_char(self): result = str_to_list('aaaa'); expected = [0]*256; expected[ord('a')] = 4; self.assertEqual(result, expected)

    def test_str_to_list_mixed_case(self): result = str_to_list('AaAa'); expected = [0]*256; expected[ord('A')] = 2; expected[ord('a')] = 2; self.assertEqual(result, expected)

    def test_str_to_list_whitespace(self): result = str_to_list('a a'); expected = [0]*256; expected[ord('a')] = 2; expected[ord(' ')] = 1; self.assertEqual(result, expected)

    def test_str_to_list_high_ascii(self): result = str_to_list(chr(255)); expected = [0]*256; expected[255] = 1; self.assertEqual(result, expected)

    def test_str_to_list_all_ascii(self): full_ascii = ''.join(chr(i) for i in range(256)); result = str_to_list(full_ascii); expected = [1]*256; self.assertEqual(result, expected)

