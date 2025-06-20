import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_031 import *

class TestVersion(unittest.TestCase):
    def test_identical_characters(self): self.assertEqual(get_Char('aaaa'), 'a')

    def test_mixed_lowercase_characters(self): self.assertEqual(get_Char('abcd'), 'b')

    def test_upper_and_lower_case(self): self.assertEqual(get_Char('aAbB'), 'Q')

    def test_symbols(self): self.assertEqual(get_Char('a!#%'), '2')

    def test_single_character(self): self.assertEqual(get_Char('Z'), 'Z')

    def test_unicode_characters(self):
        result = get_Char('你好')
        self.assertTrue(isinstance(result, str))
        self.assertEqual(len(result), 1)

    def test_numeric_characters(self): self.assertEqual(get_Char('1234'), '2')

    def test_whitespace(self): self.assertEqual(get_Char('a b'), 'K')

    def test_fractional_average(self): self.assertEqual(get_Char('ab'), 'a')

