import unittest
from datasets.o3.programs.program_071 import *

class TestVersion(unittest.TestCase):
    def test_lo_shu_magic_square(self):
        square = [[2,7,6],[9,5,1],[4,3,8]]
        self.assertTrue(magic_square_test(square))

    def test_non_magic_square_returns_false(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertFalse(magic_square_test(matrix))

    def test_four_by_four_magic_square(self):
        square = [[16,2,3,13],[5,11,10,8],[9,7,6,12],[4,14,15,1]]
        self.assertTrue(magic_square_test(square))

    def test_single_element_matrix(self):
        self.assertTrue(magic_square_test([[5]]))

    def test_non_square_matrix_raises(self):
        with self.assertRaises(IndexError):
            magic_square_test([[1,2,3],[4,5,6]])

    def test_five_by_five_magic_square(self):
        square = [[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]]
        self.assertTrue(magic_square_test(square))

