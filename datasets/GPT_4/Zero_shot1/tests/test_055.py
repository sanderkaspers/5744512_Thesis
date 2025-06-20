import unittest
from datasets.GPT_4.Zero_shot1.programs.program_055 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(merge_sorted_list([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_2(self):
        self.assertEqual(merge_sorted_list([], [1, 2]), [1, 2])

    def test_3(self):
        self.assertEqual(merge_sorted_list([], []), [])

    def test_4(self):
        self.assertEqual(merge_sorted_list([1, 2], [2, 3]), [1, 2, 2, 3])

    def test_5(self):
        self.assertEqual(merge_sorted_list([1, 4], [2, 3]), [1, 2, 3, 4])

    def test_6(self):
        self.assertEqual(merge_sorted_list([1], [2, 3, 4]), [1, 2, 3, 4])

    def test_7(self):
        self.assertEqual(merge_sorted_list([-3, -1], [-2, 0]), [-3, -2, -1, 0])

    def test_8(self):
        self.assertEqual(merge_sorted_list([1.1, 3.3], [2.2, 4.4]), [1.1, 2.2, 3.3, 4.4])

    def test_9(self):
        self.assertEqual(merge_sorted_list([3, 1], [2]), [1, 2, 3])

