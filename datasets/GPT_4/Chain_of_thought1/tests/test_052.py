import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_052 import *

class TestVersion(unittest.TestCase):
    def test_unsorted_sublists(self): self.assertEqual(sort_sublists([[3, 1], [4, 2]]), [[1, 3], [2, 4]])

    def test_sorted_sublists(self): self.assertEqual(sort_sublists([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_reverse_order(self): self.assertEqual(sort_sublists([[5, 3, 1], [2, 0]]), [[1, 3, 5], [0, 2]])

    def test_empty_sublists(self): self.assertEqual(sort_sublists([[], [1, 0]]), [[], [0, 1]])

    def test_empty_input(self): self.assertEqual(sort_sublists([]), [])

    def test_mixed_lengths(self): self.assertEqual(sort_sublists([[3, 1, 2], [5]]), [[1, 2, 3], [5]])

    def test_duplicates(self): self.assertEqual(sort_sublists([[2, 2, 1], [3, 3]]), [[1, 2, 2], [3, 3]])

    def test_negatives(self): self.assertEqual(sort_sublists([[0, -1], [-2, 3]]), [[-1, 0], [-2, 3]])

    def test_floats(self): self.assertEqual(sort_sublists([[2.1, 1.5], [3.3, 0.0]]), [[1.5, 2.1], [0.0, 3.3]])

    def test_single_element_sublists(self): self.assertEqual(sort_sublists([[5], [1]]), [[5], [1]])

    def test_mixed_empty_nonempty(self): self.assertEqual(sort_sublists([[], [3, 1]]), [[], [1, 3]])

