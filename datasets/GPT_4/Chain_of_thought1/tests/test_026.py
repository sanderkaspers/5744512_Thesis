import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_026 import *

class TestVersion(unittest.TestCase):
    def test_mixed_lengths(self): self.assertEqual(find_tuples([(1, 2), (3,), (4, 5, 6)], 2), [(1, 2)])

    def test_all_matching(self): self.assertEqual(find_tuples([(1, 2), (3, 4)], 2), [(1, 2), (3, 4)])

    def test_none_matching(self): self.assertEqual(find_tuples([(1,), (2, 3, 4)], 2), [])

    def test_includes_empty_tuple(self): self.assertEqual(find_tuples([(), (1,), (2, 3)], 0), [()])

    def test_string_tuples(self): self.assertEqual(find_tuples([('a', 'b'), ('x',)], 2), [('a', 'b')])

    def test_empty_input_list(self): self.assertEqual(find_tuples([], 2), [])

    def test_k_too_large(self): self.assertEqual(find_tuples([(1,), (2,)], 3), [])

    def test_negative_k(self): self.assertEqual(find_tuples([(1,), (2, 3)], -1), [])

    def test_with_non_tuples(self): self.assertEqual(find_tuples([(1,), [2, 3], (4, 5)], 2), [(4, 5)])

