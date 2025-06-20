import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_073 import *

class TestVersion(unittest.TestCase):
    def test_hello(self): self.assertEqual(reverse_vowels('hello'), 'holle')

    def test_leetcode(self): self.assertEqual(reverse_vowels('leetcode'), 'leotcede')

    def test_all_vowels(self): self.assertEqual(reverse_vowels('aeiou'), 'uoiea')

    def test_uppercase(self): self.assertEqual(reverse_vowels('HELLO'), 'HOLLE')

    def test_no_vowels(self): self.assertEqual(reverse_vowels('bcdfg'), 'bcdfg')

    def test_empty_string(self): self.assertEqual(reverse_vowels(''), '')

    def test_single_vowel(self): self.assertEqual(reverse_vowels('a'), 'a')

    def test_mixed_case(self): self.assertEqual(reverse_vowels('HeLLo'), 'HoLLe')

    def test_repeating(self): self.assertEqual(reverse_vowels('aA'), 'Aa')

    def test_edge_vowels(self): self.assertEqual(reverse_vowels('apple'), 'eppla')

    def test_with_symbols(self): self.assertEqual(reverse_vowels('h@e!l#l$o%'), 'h@o!l#l$e%')

    def test_one_vowel_in_middle(self): self.assertEqual(reverse_vowels('bcbob'), 'bcbob')

    def test_palindrome(self): self.assertEqual(reverse_vowels('madam'), 'madam')

    def test_vowels_and_digits(self): self.assertEqual(reverse_vowels('123aei456'), '123iea456')

