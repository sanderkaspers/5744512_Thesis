import unittest
from datasets.GPT_4.Zero_shot1.programs.program_081 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pancake_sort([3, 2, 1]), [1, 2, 3])

    def test_2(self):
        self.assertEqual(pancake_sort([3, 1, 2, 1]), [1, 1, 2, 3])

    def test_3(self):
        self.assertEqual(pancake_sort([5]), [5])

    def test_4(self):
        self.assertEqual(pancake_sort([]), [])

    def test_5(self):
        self.assertEqual(pancake_sort([4, 4, 4]), [4, 4, 4])

    def test_6(self):
        self.assertEqual(pancake_sort([-3, -1, -2]), [-3, -2, -1])

    def test_7(self):
        self.assertEqual(pancake_sort([1.1, 2.2, 0.5]), [0.5, 1.1, 2.2])

    def test_8(self):
        self.assertEqual(pancake_sort(list(range(100, 0, -1))), list(range(1, 101)))

    def test_9(self):
        self.assertTrue(all(pancake_sort([4, 2, 7, 3, 1])[i] <= pancake_sort([4, 2, 7, 3, 1])[i+1] for i in range(4)))

    def test_10(self):
        input_list = [5, 2, 3]
        pancake_sort(input_list.copy())
        self.assertEqual(input_list, [5, 2, 3])

