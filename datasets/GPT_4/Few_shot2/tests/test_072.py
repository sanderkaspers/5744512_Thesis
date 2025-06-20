import unittest
from datasets.GPT_4.Few_shot2.programs.program_072 import *

class TestVersion(unittest.TestCase):
    def test_max_occuring_char_basic(self): self.assertEqual(max_occuring_char('hello'), 'l')

    def test_max_occuring_char_tie(self): result = max_occuring_char('aabb'); self.assertIn(result, ['a', 'b'])

    def test_max_occuring_char_single(self): self.assertEqual(max_occuring_char('z'), 'z')

    def test_max_occuring_char_numbers(self): self.assertEqual(max_occuring_char('1122333'), '3')

    def test_max_occuring_char_mixed_case(self): self.assertEqual(max_occuring_char('aAbBB'), 'B')

    def test_max_occuring_char_symbols(self): self.assertEqual(max_occuring_char('!!@@@'), '@')

    def test_max_occuring_char_with_spaces(self): self.assertEqual(max_occuring_char('a a a b'), 'a')

    def test_max_occuring_char_all_unique(self): result = max_occuring_char('abcd'); self.assertIn(result, ['a', 'b', 'c', 'd'])

