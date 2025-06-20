import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_006 import *

class TestVersion(unittest.TestCase):
    def test_lowercase_only(self): result = str_to_list('abcabc'); self.assertEqual(result[ord('a')], 2); self.assertEqual(result[ord('b')], 2); self.assertEqual(result[ord('c')], 2)

    def test_mixed_case(self): result = str_to_list('AaBb'); self.assertEqual(result[ord('A')], 1); self.assertEqual(result[ord('a')], 1); self.assertEqual(result[ord('B')], 1); self.assertEqual(result[ord('b')], 1)

    def test_digits(self): result = str_to_list('112233'); self.assertEqual(result[ord('1')], 2); self.assertEqual(result[ord('2')], 2); self.assertEqual(result[ord('3')], 2)

    def test_special_characters(self): result = str_to_list('@#@!'); self.assertEqual(result[ord('@')], 2); self.assertEqual(result[ord('#')], 1); self.assertEqual(result[ord('!')], 1)

    def test_repeated_character(self): result = str_to_list('zzzzz'); self.assertEqual(result[ord('z')], 5)

    def test_empty_string(self): result = str_to_list(''); self.assertEqual(sum(result), 0)

    def test_all_ascii_chars(self): ascii_chars = ''.join(chr(i) for i in range(256)); result = str_to_list(ascii_chars); [self.assertEqual(result[i], 1) for i in range(256)]

    def test_whitespace_characters(self): result = str_to_list(' \t\n'); self.assertEqual(result[ord(' ')], 1); self.assertEqual(result[ord('\t')], 1); self.assertEqual(result[ord('\n')], 1)

    def test_control_characters(self): ctrl_str = '\x00\x01\x02'; result = str_to_list(ctrl_str); self.assertEqual(result[0], 1); self.assertEqual(result[1], 1); self.assertEqual(result[2], 1)

