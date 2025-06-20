import unittest
from datasets.GPT_4.Few_shot2.programs.program_042 import *

class TestVersion(unittest.TestCase):
    def test_index_minimum_basic(self): self.assertEqual(index_minimum([(1, 2), (3, 1), (5, 0)]), (5, 0))

    def test_index_minimum_all_equal(self): self.assertEqual(index_minimum([(1, 2), (3, 2), (5, 2)]), (1, 2))

    def test_index_minimum_single_element(self): self.assertEqual(index_minimum([(7, 4)]), (7, 4))

    def test_index_minimum_negative_values(self): self.assertEqual(index_minimum([(2, -5), (1, -10), (3, -1)]), (1, -10))

    def test_index_minimum_mixed_values(self): self.assertEqual(index_minimum([(0, 0), (10, -1), (-5, 1)]), (10, -1))

    def test_index_minimum_floats(self): self.assertEqual(index_minimum([(1.1, 3.5), (2.2, 2.1), (3.3, 1.0)]), (3.3, 1.0))

    def test_index_minimum_with_duplicates(self): self.assertEqual(index_minimum([(2, 2), (3, 1), (4, 1)]), (3, 1))

    def test_index_minimum_large_input(self): self.assertEqual(index_minimum([(i, i*i) for i in range(100)]), (0, 0))

    def test_index_minimum_tied_but_first_returned(self): self.assertEqual(index_minimum([(9, 1), (8, 1), (7, 1)]), (9, 1))

    def test_index_minimum_complex_types(self): self.assertEqual(index_minimum([('a', 5), ('b', 3)]), ('b', 3))

