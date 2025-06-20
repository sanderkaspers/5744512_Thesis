import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_045 import *

class TestVersion(unittest.TestCase):
    def test_non_overlapping_elements(self): self.assertEqual(frequency_lists([[1, 2], [3, 4]]), {1: 1, 2: 1, 3: 1, 4: 1})

    def test_with_duplicates_across_sublists(self): self.assertEqual(frequency_lists([[1, 2], [2, 3], [1]]), {1: 2, 2: 2, 3: 1})

    def test_all_same_elements(self): self.assertEqual(frequency_lists([[5, 5], [5], [5, 5]]), {5: 5})

    def test_mixed_types(self): self.assertEqual(frequency_lists([[1, 'a'], ['a', 1]]), {1: 2, 'a': 2})

    def test_empty_outer_list(self): self.assertEqual(frequency_lists([]), {})

    def test_some_empty_sublists(self): self.assertEqual(frequency_lists([[], [1], [], [1, 2]]), {1: 2, 2: 1})

    def test_all_empty_sublists(self): self.assertEqual(frequency_lists([[], [], []]), {})

    def test_single_element_sublists(self): self.assertEqual(frequency_lists([[1], [2], [3]]), {1: 1, 2: 1, 3: 1})

    def test_large_list(self): self.assertEqual(frequency_lists([[i for i in range(100)] for _ in range(10)]), {i: 10 for i in range(100)})

