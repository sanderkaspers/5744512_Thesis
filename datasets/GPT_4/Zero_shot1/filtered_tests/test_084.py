import unittest
from datasets.GPT_4.Zero_shot1.programs.program_084 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_Abs_Diff([-5, -2, -9]), 7)

    def test_2(self):
        self.assertEqual(max_Abs_Diff([-3, 0, 5]), 8)

    def test_3(self):
        self.assertEqual(max_Abs_Diff([7]), 0)

    def test_4(self):
        self.assertEqual(max_Abs_Diff([2, 2, 2]), 0)

    def test_5(self):
        self.assertEqual(max_Abs_Diff([5, 3, 9, 1]), 8)

    def test_6(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5]), 4)

    def test_7(self):
        self.assertEqual(max_Abs_Diff([5, 4, 3, 2, 1]), 4)

    def test_8(self):
        self.assertEqual(max_Abs_Diff([1.1, 2.5, -3.0]), 5.5)

    def test_9(self):
        self.assertIsInstance(max_Abs_Diff([1, 2, 3]), (int, float))

