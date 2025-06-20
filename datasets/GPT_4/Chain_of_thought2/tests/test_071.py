import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_071 import *

class TestVersion(unittest.TestCase):
    def test_3x3_magic_square(self): self.assertTrue(magic_square_test([[2,7,6],[9,5,1],[4,3,8]]))

    def test_non_magic_square(self): self.assertFalse(magic_square_test([[1,2,3],[4,5,6],[7,8,9]]))

    def test_1x1_magic_square(self): self.assertTrue(magic_square_test([[5]]))

    def test_2x2_non_magic_square(self): self.assertFalse(magic_square_test([[1,2],[3,4]]))

    def test_4x4_magic_square(self): self.assertTrue(magic_square_test([[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]))

    def test_negative_numbers_magic_square(self): self.assertTrue(magic_square_test([[-2,-7,-6],[-9,-5,-1],[-4,-3,-8]]))

