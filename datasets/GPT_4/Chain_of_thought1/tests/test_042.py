import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_042 import *

class TestVersion(unittest.TestCase):
    def test_simple_min(self): self.assertEqual(index_min([(1, 3), (2, 2), (3, 1)]), 2)

    def test_tie_min(self): self.assertEqual(index_min([(1, 2), (2, 2), (3, 5)]), 0)

    def test_all_equal(self): self.assertEqual(index_min([(1, 1), (2, 1), (3, 1)]), 0)

    def test_negative_values(self): self.assertEqual(index_min([(1, -1), (2, -5), (3, 0)]), 1)

    def test_single_tuple(self): self.assertEqual(index_min([(42, 99)]), 0)

    def test_extra_elements(self): self.assertEqual(index_min([(1, 4, 7), (2, 3, 6), (3, 2, 5)]), 2)

    def test_float_values(self): self.assertEqual(index_min([(1, 1.5), (2, 0.5), (3, 2.0)]), 1)

