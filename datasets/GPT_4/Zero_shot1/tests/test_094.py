import unittest
from datasets.GPT_4.Zero_shot1.programs.program_094 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_range_list([1, 2, 3], 0, 0), 1)

    def test_2(self):
        self.assertEqual(sum_range_list([1, 2, 3], 0, 2), 6)

    def test_3(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4], -1, 2), 9)

    def test_4(self):
        self.assertEqual(sum_range_list([5], 0, 0), 5)

    def test_5(self):
        self.assertEqual(sum_range_list([-1, -2, -3], 0, 2), -6)

    def test_6(self):
        self.assertIsInstance(sum_range_list([1.5, 2.5, 3.0], 0, 2), float)

    def test_7(self):
        self.assertEqual(sum_range_list([10, 20, 30, 40, 50], 2, 3), 70)

