import unittest
from datasets.GPT_4.Few_shot1.programs.program_071 import *

class TestVersion(unittest.TestCase):
    def test_magic_square_true_3x3(self): self.assertEqual(magic_square_test([[2,7,6],[9,5,1],[4,3,8]]), True)

    def test_magic_square_false_row_sum(self): self.assertEqual(magic_square_test([[2,7,6],[9,5,1],[4,3,7]]), False)

    def test_magic_square_false_column_sum(self): self.assertEqual(magic_square_test([[8,1,6],[3,5,7],[4,9,2]]), True)

    def test_magic_square_false_diagonal(self): self.assertEqual(magic_square_test([[8,1,6],[3,5,7],[4,9,3]]), False)

    def test_magic_square_single_element(self): self.assertEqual(magic_square_test([[5]]), True)

    def test_magic_square_2x2_false(self): self.assertEqual(magic_square_test([[1,2],[3,4]]), False)

    def test_magic_square_non_square(self): self.assertEqual(magic_square_test([[1,2,3],[4,5,6]]), False)

    def test_magic_square_row_column_mismatch(self): self.assertEqual(magic_square_test([[1,2],[2,1]]), False)

    def test_magic_square_true_4x4(self): self.assertEqual(magic_square_test([[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]), True)

