import unittest
from datasets.GPT_4.Zero_shot2.programs.program_015 import *

class TestVersion(unittest.TestCase):
    def test_diff_1(self):
        self.assertEqual(max_difference([0, 1, 2, 3]), 3)

    def test_diff_2(self):
        self.assertEqual(max_difference([3, 2, 1, 0]), 3)

    def test_diff_3(self):
        self.assertEqual(max_difference([0, 1, 2]), 0)

    def test_diff_4(self):
        self.assertEqual(max_difference([-1, -2, -3]), 4)

    def test_diff_5(self):
        self.assertEqual(max_difference([5, 5, 5, 5]), 3)

    def test_diff_6(self):
        self.assertEqual(max_difference([10]), 10)

