import unittest
from datasets.GPT_4.Few_shot2.programs.program_036 import *

class TestVersion(unittest.TestCase):
    def test_freq_count_basic(self): self.assertEqual(freq_count(['a', 'b', 'a']), {'a': 2, 'b': 1})

    def test_freq_count_all_unique(self): self.assertEqual(freq_count(['x', 'y', 'z']), {'x': 1, 'y': 1, 'z': 1})

    def test_freq_count_all_same(self): self.assertEqual(freq_count(['a', 'a', 'a']), {'a': 3})

    def test_freq_count_empty_list(self): self.assertEqual(freq_count([]), {})

    def test_freq_count_numbers(self): self.assertEqual(freq_count([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})

    def test_freq_count_mixed_types(self): self.assertEqual(freq_count([1, '1', 1, '1']), {1: 2, '1': 2})

    def test_freq_count_single_element(self): self.assertEqual(freq_count(['only']), {'only': 1})

    def test_freq_count_large_input(self): self.assertEqual(freq_count([0]*1000), {0: 1000})

    def test_freq_count_boolean(self): self.assertEqual(freq_count([True, False, True]), {True: 2, False: 1})

