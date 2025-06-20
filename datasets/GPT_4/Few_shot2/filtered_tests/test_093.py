import unittest
from datasets.GPT_4.Few_shot2.programs.program_093 import *

class TestVersion(unittest.TestCase):
    def test_frequency_present_multiple(self): self.assertEqual(frequency([1, 2, 2, 3], 2), 2)

    def test_frequency_present_once(self): self.assertEqual(frequency([1, 2, 3], 3), 1)

    def test_frequency_not_present(self): self.assertEqual(frequency([1, 2, 3], 4), 0)

    def test_frequency_empty_list(self): self.assertEqual(frequency([], 1), 0)

    def test_frequency_all_same(self): self.assertEqual(frequency([5, 5, 5], 5), 3)

    def test_frequency_all_different(self): self.assertEqual(frequency([1, 2, 3], 0), 0)

    def test_frequency_with_strings(self): self.assertEqual(frequency(['a', 'b', 'a'], 'a'), 2)

    def test_frequency_with_mixed_types(self): self.assertEqual(frequency([1, '1', 1.0], 1), 2)

    def test_frequency_single_element(self): self.assertEqual(frequency([7], 7), 1)

