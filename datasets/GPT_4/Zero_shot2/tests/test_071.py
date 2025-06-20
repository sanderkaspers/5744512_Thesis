import unittest
from datasets.GPT_4.Zero_shot2.programs.program_071 import *

class TestVersion(unittest.TestCase):
    def test_magic_1(self):
        self.assertTrue(magic_square_test([[8, 1, 6], [3, 5, 7], [4, 9, 2]]))

    def test_magic_2(self):
        self.assertFalse(magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 9]]))

    def test_magic_3(self):
        self.assertFalse(magic_square_test([[8, 1, 6], [3, 5, 7], [4, 8, 2]]))

    def test_magic_4(self):
        self.assertFalse(magic_square_test([[8, 1, 6], [3, 5, 7], [2, 9, 4]]))

    def test_magic_5(self):
        self.assertTrue(magic_square_test([[5]]))

    def test_magic_6(self):
        self.assertFalse(magic_square_test([[-2, -7, -6], [-9, -5, -1], [-4, -3, -8]]))

    def test_magic_7(self):
        self.assertTrue(magic_square_test([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]))

    def test_magic_8(self):
        self.assertFalse(magic_square_test([[6, 7, 2], [1, 5, 9], [8, 3, 4]]))

