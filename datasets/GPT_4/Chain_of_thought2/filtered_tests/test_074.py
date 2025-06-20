import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_074 import *

class TestVersion(unittest.TestCase):
    def test_basic_char_tuple(self): self.assertEqual(tup_string(('H','e','l','l','o')), 'Hello')

    def test_tuple_of_digits(self): self.assertEqual(tup_string(('1','2','3')), '123')

    def test_tuple_with_space(self): self.assertEqual(tup_string(('a',' ','b')), 'a b')

    def test_empty_tuple(self): self.assertEqual(tup_string(()), '')

    def test_tuple_with_symbols(self): self.assertEqual(tup_string(('!','@','#')), '!@#')

    def test_single_element_tuple(self): self.assertEqual(tup_string(('Z',)), 'Z')

    def test_mixed_case_letters(self): self.assertEqual(tup_string(('A','b','C')), 'AbC')

    def test_tuple_with_newline(self): self.assertEqual(tup_string(('a','\n','b')), 'a\nb')

    def test_long_tuple(self): self.assertEqual(tup_string(tuple('abc'*10)), 'abc'*10)

