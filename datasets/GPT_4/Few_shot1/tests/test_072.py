import unittest
from datasets.GPT_4.Few_shot1.programs.program_072 import *

class TestVersion(unittest.TestCase):
    def test_max_occurrences_basic(self): self.assertEqual(max_occurrences([1, 2, 2, 3]), 2)

    def test_max_occurrences_all_unique(self): self.assertEqual(max_occurrences([4, 5, 6]), 4)

    def test_max_occurrences_single_element(self): self.assertEqual(max_occurrences([7]), 7)

    def test_max_occurrences_all_same(self): self.assertEqual(max_occurrences([3, 3, 3]), 3)

    def test_max_occurrences_multiple_modes(self): self.assertEqual(max_occurrences([1, 2, 1, 2]), 1)

    def test_max_occurrences_negative_numbers(self): self.assertEqual(max_occurrences([-1, -1, -2]), -1)

    def test_max_occurrences_mixed_signs(self): self.assertEqual(max_occurrences([-3, 1, -3, 1, 1]), 1)

    def test_max_occurrences_large_list(self): self.assertEqual(max_occurrences([1]*100 + [2]*99), 1)

    def test_max_occurrences_strings(self): self.assertEqual(max_occurrences(["a", "b", "a", "c", "a"]), "a")

