import unittest
from datasets.GPT_4.Zero_shot1.programs.program_071 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertTrue(magic_square_test([[2,7,6],[9,5,1],[4,3,8]]))

    def test_2(self):
        self.assertFalse(magic_square_test([[2,7,6],[9,5,1],[4,3,7]]))

    def test_3(self):
        self.assertFalse(magic_square_test([[2,7,6],[9,5,1],[5,3,8]]))

    def test_4(self):
        self.assertFalse(magic_square_test([[2,7,6],[9,5,1],[4,2,8]]))

    def test_5(self):
        self.assertTrue(magic_square_test([[5]]))

    def test_6(self):
        self.assertFalse(magic_square_test([[1,2],[3,4]]))

    def test_7(self):
        result = magic_square_test([[2,7,6],[9,5,1],[4,3,8]])
        self.assertIsInstance(result, bool)

