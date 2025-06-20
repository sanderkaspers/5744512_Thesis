import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_093 import *

class TestVersion(unittest.TestCase):
    def test_multiple_occurrences(self): self.assertEqual(frequency([1, 2, 3, 1, 1], 1), 3)

    def test_single_occurrence(self): self.assertEqual(frequency([5, 6, 7], 6), 1)

    def test_no_occurrence(self): self.assertEqual(frequency([5, 6, 7], 9), 0)

    def test_string_occurrence(self): self.assertEqual(frequency(['a', 'b', 'a'], 'a'), 2)

    def test_mixed_type_equality(self): self.assertEqual(frequency([1, '1', 1.0], 1), 2)

    def test_empty_list(self): self.assertEqual(frequency([], 5), 0)

    def test_none_value(self): self.assertEqual(frequency([None, 1, None], None), 2)

    def test_search_list_element(self): self.assertEqual(frequency([[1], [2], [1]], [1]), 2)

    def test_boolean_equivalence(self): self.assertEqual(frequency([True, False, 1], True), 2)

    def test_float_equivalence(self): self.assertEqual(frequency([1.0, 1.00, 1], 1), 3)

    def test_case_sensitivity(self): self.assertEqual(frequency(['a', 'A'], 'a'), 1)

