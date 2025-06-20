import unittest
from datasets.mbpp.programs.program_002 import *

class TestVersion(unittest.TestCase):
    def test_sort_matrix_with_1_2_3_2_4_5_1_1_1(self):
        self.assertEqual(
        sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]),
        [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
        )

    def test_sort_matrix_with_5_8_9_6_4_3_2_1_4(self):
        self.assertEqual(
        sort_matrix([[5,8,9],[6,4,3],[2,1,4]]),
        [[2, 1, 4], [6, 4, 3], [5, 8, 9]]
        )

    def test_sort_matrix_with_1_2_3__2_4__5_1__1_1(self):
        self.assertEqual(
        sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]]),
        [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
        )

