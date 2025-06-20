import unittest
from datasets.GPT_4.Few_shot2.programs.program_074 import *

class TestVersion(unittest.TestCase):
    def test_tup_string_basic(self): self.assertEqual(tup_string(('h', 'e', 'l', 'l', 'o')), 'hello')

    def test_tup_string_empty(self): self.assertEqual(tup_string(()), '')

    def test_tup_string_single_element(self): self.assertEqual(tup_string(('x',)), 'x')

    def test_tup_string_with_spaces(self): self.assertEqual(tup_string(('a', ' ', 'b')), 'a b')

    def test_tup_string_with_symbols(self): self.assertEqual(tup_string(('!', '@', '#')), '!@#')

    def test_tup_string_numeric_characters(self): self.assertEqual(tup_string(('1', '2', '3')), '123')

    def test_tup_string_mixed_characters(self): self.assertEqual(tup_string(('a', '1', '!')), 'a1!')

    def test_tup_string_unicode_characters(self): self.assertEqual(tup_string(('你', '好')), '你好')

    def test_tup_string_long_tuple(self): self.assertEqual(tup_string(tuple('abcdef')), 'abcdef')

