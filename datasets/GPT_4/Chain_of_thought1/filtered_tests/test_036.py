import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_036 import *

class TestVersion(unittest.TestCase):
    def test_mixed_repeats(self): self.assertEqual(freq_count(['a', 'b', 'a', 'c']), {'a': 2, 'b': 1, 'c': 1})

    def test_all_unique(self): self.assertEqual(freq_count(['x', 'y', 'z']), {'x': 1, 'y': 1, 'z': 1})

    def test_all_same(self): self.assertEqual(freq_count(['a', 'a', 'a']), {'a': 3})

    def test_empty_list(self): self.assertEqual(freq_count([]), {})

    def test_integer_list(self): self.assertEqual(freq_count([1, 2, 1, 3]), {1: 2, 2: 1, 3: 1})

    def test_mixed_types(self): self.assertEqual(freq_count(['a', 1, 'a', 1]), {'a': 2, 1: 2})

    def test_booleans(self): self.assertEqual(freq_count([True, False, True]), {True: 2, False: 1})

    def test_special_chars(self): self.assertEqual(freq_count(['!', '@', '!', '#']), {'!': 2, '@': 1, '#': 1})

