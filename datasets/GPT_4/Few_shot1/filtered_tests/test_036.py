import unittest
from datasets.GPT_4.Few_shot1.programs.program_036 import *

class TestVersion(unittest.TestCase):
    def test_freq_count_basic(self): self.assertEqual(freq_count(['a', 'b', 'a']), {'a': 2, 'b': 1})

    def test_freq_count_numbers(self): self.assertEqual(freq_count([1, 2, 2, 3, 1]), {1: 2, 2: 2, 3: 1})

    def test_freq_count_empty(self): self.assertEqual(freq_count([]), {})

    def test_freq_count_all_unique(self): self.assertEqual(freq_count(['x', 'y', 'z']), {'x': 1, 'y': 1, 'z': 1})

    def test_freq_count_all_same(self): self.assertEqual(freq_count(['same'] * 5), {'same': 5})

    def test_freq_count_mixed_types(self): self.assertEqual(freq_count([1, '1', 1.0]), {1: 2, '1': 1})

