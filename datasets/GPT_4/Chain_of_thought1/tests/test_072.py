import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_072 import *

class TestVersion(unittest.TestCase):
    def test_clear_max(self): self.assertEqual(max_occurrences([1, 2, 2, 3]), 2)

    def test_tie(self): result = max_occurrences([1, 2, 1, 2]); self.assertIn(result, [1, 2])

    def test_single_element(self): self.assertEqual(max_occurrences([7]), 7)

    def test_all_unique(self): result = max_occurrences([1, 2, 3, 4]); self.assertIn(result, [1, 2, 3, 4])

    def test_strings(self): self.assertEqual(max_occurrences(['a', 'b', 'a', 'c']), 'a')

    def test_mixed_types(self): self.assertEqual(max_occurrences([1, '1', 1]), 1)

    def test_negatives(self): self.assertEqual(max_occurrences([-1, -2, -1]), -1)

    def test_none_elements(self): self.assertEqual(max_occurrences([None, None, 1]), None)

    def test_large_input(self): self.assertEqual(max_occurrences([1]*1000 + [2]*500), 1)

    def test_boolean_list(self): self.assertEqual(max_occurrences([True, False, True]), True)

