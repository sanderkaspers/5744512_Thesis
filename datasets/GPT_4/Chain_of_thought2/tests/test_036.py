import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_036 import *

class TestVersion(unittest.TestCase):
    def test_all_unique(self): self.assertEqual(freq_count(['a', 'b', 'c']), Counter({'a': 1, 'b': 1, 'c': 1}))

    def test_all_identical(self): self.assertEqual(freq_count(['x', 'x', 'x']), Counter({'x': 3}))

    def test_some_duplicates(self): self.assertEqual(freq_count(['a', 'b', 'a', 'c', 'b']), Counter({'a': 2, 'b': 2, 'c': 1}))

    def test_empty_list(self): self.assertEqual(freq_count([]), Counter())

    def test_numeric_elements(self): self.assertEqual(freq_count([1, 2, 2, 3, 1, 1]), Counter({1: 3, 2: 2, 3: 1}))

    def test_mixed_types(self): self.assertEqual(freq_count([1, '1', 1.0, True]), Counter({1: 2, '1': 1}))

    def test_with_none_and_bool(self): self.assertEqual(freq_count([None, True, False, None, True]), Counter({None: 2, True: 2, False: 1}))

    def test_with_tuple_keys(self): self.assertEqual(freq_count([(1, 2), (1, 2), (3, 4)]), Counter({(1, 2): 2, (3, 4): 1}))

    def test_large_input(self): data = ['x'] * 10000 + ['y'] * 5000; self.assertEqual(freq_count(data), Counter({'x': 10000, 'y': 5000}))

