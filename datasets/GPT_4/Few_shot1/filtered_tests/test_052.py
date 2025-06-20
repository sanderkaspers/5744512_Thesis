import unittest
from datasets.GPT_4.Few_shot1.programs.program_052 import *

class TestVersion(unittest.TestCase):
    def test_sort_sublists_basic(self): self.assertEqual(sort_sublists([[(3, 2), (1, 4)]]), [[(1, 4), (3, 2)]])

    def test_sort_sublists_multiple(self): self.assertEqual(sort_sublists([[(2, 3), (1, 2)], [(4, 5), (3, 6)]]), [[(1, 2), (2, 3)], [(3, 6), (4, 5)]])

    def test_sort_sublists_empty(self): self.assertEqual(sort_sublists([]), [])

    def test_sort_sublists_with_empty_inner(self): self.assertEqual(sort_sublists([[], [(1, 2), (0, 1)]]), [[], [(0, 1), (1, 2)]])

    def test_sort_sublists_already_sorted(self): self.assertEqual(sort_sublists([[(1, 2), (2, 3)]]), [[(1, 2), (2, 3)]])

    def test_sort_sublists_same_keys(self): self.assertEqual(sort_sublists([[(2, 5), (2, 1)]]), [[(2, 5), (2, 1)]])

