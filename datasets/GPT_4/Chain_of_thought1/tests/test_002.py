import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_002 import *

class TestVersion(unittest.TestCase):
    def test_typical_2_element_rows(self): self.assertEqual(sort_matrix([[1, 3], [2, 1], [3, 2]]), [[2, 1], [3, 2], [1, 3]])

    def test_3_element_rows(self): self.assertEqual(sort_matrix([[1, 5, 9], [2, 3, 8], [3, 7, 1]]), [[2, 3, 8], [1, 5, 9], [3, 7, 1]])

    def test_already_sorted(self): self.assertEqual(sort_matrix([[1, 1], [2, 2], [3, 3]]), [[1, 1], [2, 2], [3, 3]])

    def test_repeated_second_elements(self): self.assertEqual(sort_matrix([[1, 2], [2, 1], [3, 2]]), [[2, 1], [1, 2], [3, 2]])

    def test_negative_second_elements(self): self.assertEqual(sort_matrix([[1, -3], [2, 0], [3, -1]]), [[1, -3], [3, -1], [2, 0]])

    def test_empty_matrix(self): self.assertEqual(sort_matrix([]), [])

    def test_single_row_matrix(self): self.assertEqual(sort_matrix([[5, 10]]), [[5, 10]])

    def test_float_and_integer_elements(self): self.assertEqual(sort_matrix([[1, 3.5], [2, 2], [3, 4.1]]), [[2, 2], [1, 3.5], [3, 4.1]])

    def test_string_second_elements(self): self.assertEqual(sort_matrix([['a', 'dog'], ['b', 'apple'], ['c', 'car']]), [['b', 'apple'], ['c', 'car'], ['a', 'dog']])

