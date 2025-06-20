import unittest
from datasets.GPT_4.Zero_shot2.programs.program_081 import *

class TestVersion(unittest.TestCase):
    def test_pancake_1(self):
        self.assertEqual(pancake_sort([1, 2, 3]), [1, 2, 3])

    def test_pancake_2(self):
        self.assertEqual(pancake_sort([3, 2, 1]), [1, 2, 3])

    def test_pancake_3(self):
        self.assertEqual(pancake_sort([4, 3, 1, 2]), [1, 2, 3, 4])

    def test_pancake_4(self):
        self.assertEqual(pancake_sort([1, 3, 3, 2]), [1, 2, 3, 3])

    def test_pancake_5(self):
        self.assertEqual(pancake_sort([]), [])

    def test_pancake_6(self):
        self.assertEqual(pancake_sort([5]), [5])

    def test_pancake_7(self):
        self.assertEqual(pancake_sort([2, 2, 2]), [2, 2, 2])

    def test_pancake_8(self):
        self.assertEqual(pancake_sort([-3, -1, -2]), [-3, -2, -1])

    def test_pancake_9(self):
        self.assertEqual(pancake_sort([0, -1, 2, -3]), [-3, -1, 0, 2])

    def test_pancake_10(self):
        self.assertEqual(pancake_sort(list(range(10, 0, -1))), list(range(1, 11)))

