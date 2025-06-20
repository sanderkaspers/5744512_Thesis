import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_072 import *

class TestVersion(unittest.TestCase):
    def test_single_max_occurrence(self): self.assertEqual(max_occurrences([1,2,2,3]), 2)

    def test_all_unique_elements(self): self.assertEqual(max_occurrences([1,2,3,4]), 1)

    def test_multiple_same_max_frequencies(self): self.assertEqual(max_occurrences([1,1,2,2]), 1)

    def test_with_negative_numbers(self): self.assertEqual(max_occurrences([-1,-1,0,0,0]), 0)

    def test_with_mixed_types(self): self.assertEqual(max_occurrences(['a', 'b', 'a', 1, 1, 1]), 1)

    def test_with_strings(self): self.assertEqual(max_occurrences(['apple','banana','apple','cherry']), 'apple')

    def test_single_element_list(self): self.assertEqual(max_occurrences([42]), 42)

    def test_large_input(self): self.assertEqual(max_occurrences([5]*1000 + [1]*999), 5)

