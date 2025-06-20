import unittest
from datasets.GPT_4.Zero_shot2.programs.program_023 import *

class TestVersion(unittest.TestCase):
    def test_comb_1(self):
        self.assertEqual(comb_sort([3, 1, 2]), [1, 2, 3])

    def test_comb_2(self):
        self.assertEqual(comb_sort([1, 2, 3]), [1, 2, 3])

    def test_comb_3(self):
        self.assertEqual(comb_sort([3, 2, 1]), [1, 2, 3])

    def test_comb_4(self):
        self.assertEqual(comb_sort([3, 1, 2, 1]), [1, 1, 2, 3])

    def test_comb_5(self):
        self.assertEqual(comb_sort([-3, -1, -2]), [-3, -2, -1])

    def test_comb_6(self):
        self.assertEqual(comb_sort([10]), [10])

    def test_comb_7(self):
        self.assertEqual(comb_sort([]), [])

    def test_comb_8(self):
        self.assertEqual(comb_sort([5, 5, 5]), [5, 5, 5])

