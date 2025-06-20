import unittest
from datasets.GPT_4.Few_shot.programs.program_071 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]]), True) # 3x3 Magic Square)

    def test_case_2(self):
        self.assertEqual(magic_square_test([[1, 2], [2, 1]]), False) # 2x2 Non-Magic Square)

    def test_case_3(self):
        self.assertEqual(magic_square_test([[4, 9, 2], [3, 5, 7], [8, 1, 6]]), True) # Another 3x3 Magic Square)

    def test_case_4(self):
        self.assertEqual(magic_square_test([[10, 20], [20, 10]]), False) # 2x2 with different sums)

    def test_case_5(self):
        self.assertEqual(magic_square_test([[5]]), True) # 1x1 Matrix, trivially magic)

    def test_case_6(self):
        self.assertEqual(magic_square_test([[16, 23, 17], [78, 32, 25], [0, 21, 45]]), False) # 3x3 Non-Magic)

    def test_case_7(self):
        self.assertEqual(magic_square_test([[8, 1, 6], [3, 5, 7], [4, 9, 2]]), True) # Reversed 3x3 Magic Square)

    def test_case_8(self):
        self.assertEqual(magic_square_test([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), False) # Consecutive numbers, not magic)

