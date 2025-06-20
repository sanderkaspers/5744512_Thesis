import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_071 import *

class TestVersion(unittest.TestCase):
    def test_3x3_magic_square(self): self.assertTrue(magic_square_test([[8, 1, 6], [3, 5, 7], [4, 9, 2]]))

    def test_4x4_magic_square(self): self.assertTrue(magic_square_test([[16, 2, 3, 13], [5, 11, 10, 8], [9, 7, 6, 12], [4, 14, 15, 1]]))

    def test_non_magic(self): self.assertFalse(magic_square_test([[8, 1, 6], [3, 5, 7], [4, 9, 3]]))

    def test_2x2_non_magic(self): self.assertFalse(magic_square_test([[1, 2], [3, 4]]))

    def test_1x1_matrix(self): self.assertTrue(magic_square_test([[7]]))

    def test_all_equal(self): self.assertTrue(magic_square_test([[5, 5], [5, 5]]))

    def test_negative_magic(self): self.assertTrue(magic_square_test([[-2, -1, -3], [-3, -2, -1], [-1, -3, -2]]))

