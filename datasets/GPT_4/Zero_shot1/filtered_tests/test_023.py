import unittest
from datasets.GPT_4.Zero_shot1.programs.program_023 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(comb_sort([3, 2, 1]), [1, 2, 3])

    def test_2(self):
        self.assertEqual(comb_sort([4, 5, 4, 5]), [4, 4, 5, 5])

    def test_3(self):
        self.assertEqual(comb_sort([42]), [42])

    def test_4(self):
        self.assertEqual(comb_sort([]), [])

    def test_5(self):
        self.assertEqual(comb_sort([-1, -5, -3]), [-5, -3, -1])

    def test_6(self):
        self.assertEqual(comb_sort([1.1, 3.3, 2.2]), [1.1, 2.2, 3.3])

    def test_7(self):
        self.assertEqual(comb_sort([7, 7, 7, 7]), [7, 7, 7, 7])

    def test_8(self):
        self.assertEqual(comb_sort([-3, 0, 2, -1, 1]), [-3, -1, 0, 1, 2])

