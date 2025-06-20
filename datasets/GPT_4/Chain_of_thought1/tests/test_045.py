import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_045 import *

class TestVersion(unittest.TestCase):
    def test_mixed_freq(self): self.assertEqual(frequency_lists(['a', 'b', 'a', 'c', 'b', 'b']), [('b', 3), ('a', 2), ('c', 1)])

    def test_all_unique(self): self.assertEqual(frequency_lists(['x', 'y', 'z']), [('x', 1), ('y', 1), ('z', 1)])

    def test_all_same(self): self.assertEqual(frequency_lists(['a', 'a', 'a']), [('a', 3)])

    def test_some_repeated(self): self.assertEqual(frequency_lists(['a', 'b', 'a', 'c']), [('a', 2), ('b', 1), ('c', 1)])

    def test_with_empty_strings(self): self.assertEqual(frequency_lists(['', 'a', '', 'b', 'a']), [('a', 2), ('b', 1)])

    def test_only_empty_strings(self): self.assertEqual(frequency_lists(['', '', '']), [])

    def test_case_sensitive(self): self.assertEqual(frequency_lists(['A', 'a', 'A', 'a', 'a']), [('a', 3), ('A', 2)])

    def test_empty_list(self): self.assertEqual(frequency_lists([]), [])

    def test_mixed_types(self): self.assertEqual(frequency_lists([1, '1', 1, '1', 2]), [(1, 2), ('1', 2), (2, 1)])

    def test_numeric_list(self): self.assertEqual(frequency_lists([5, 5, 3, 3, 3]), [(3, 3), (5, 2)])

    def test_with_none(self): self.assertEqual(frequency_lists([None, 'a', None, 'a', 'b']), [('a', 2), (None, 2), ('b', 1)])

