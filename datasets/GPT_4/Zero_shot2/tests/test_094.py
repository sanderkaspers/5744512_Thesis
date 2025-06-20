import unittest
from datasets.GPT_4.Zero_shot2.programs.program_094 import *

class TestVersion(unittest.TestCase):
    def test_range_1(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 4), 9)

    def test_range_2(self):
        self.assertEqual(sum_range_list([1, 2, 3], 5, 10), 0)

    def test_range_3(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 5), 15)

    def test_range_4(self):
        self.assertEqual(sum_range_list([-3, -2, -1, 0, 1], -2, 0), -3)

    def test_range_5(self):
        self.assertEqual(sum_range_list([1, 2, 3], 4, 3), 0)

    def test_range_6(self):
        self.assertEqual(sum_range_list([1, 2, 3], 2, 2), 2)

    def test_range_7(self):
        self.assertEqual(sum_range_list([1, 3, 5], 2, 2), 0)

    def test_range_8(self):
        self.assertEqual(sum_range_list([], 0, 10), 0)

    def test_range_9(self):
        self.assertEqual(sum_range_list([1, 1, 2, 2, 3], 2, 2), 4)

    def test_range_10(self):
        self.assertEqual(sum_range_list([1, 'a', 3], 1, 3), 4)

