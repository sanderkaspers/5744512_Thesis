import unittest
from datasets.GPT_4.Few_shot2.programs.program_071 import *

class TestVersion(unittest.TestCase):
    def test_magic_square_valid_3x3(self): self.assertTrue(magic_square_test([[2, 7, 6],[9, 5, 1],[4, 3, 8]]))

    def test_magic_square_valid_1x1(self): self.assertTrue(magic_square_test([[5]]))

    def test_magic_square_invalid_row_sum(self): self.assertFalse(magic_square_test([[2, 7, 6],[9, 5, 1],[4, 3, 9]]))

    def test_magic_square_invalid_column_sum(self): self.assertFalse(magic_square_test([[2, 7, 6],[9, 5, 1],[4, 2, 8]]))

    def test_magic_square_invalid_diagonal_sum(self): self.assertFalse(magic_square_test([[2, 7, 6],[9, 4, 1],[4, 3, 8]]))

    def test_magic_square_valid_4x4(self): self.assertTrue(magic_square_test([[16, 3, 2, 13],[5, 10, 11, 8],[9, 6, 7, 12],[4, 15, 14, 1]]))

