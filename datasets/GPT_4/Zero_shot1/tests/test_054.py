import unittest
from datasets.GPT_4.Zero_shot1.programs.program_054 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add_lists([1, 2], (3, 4)), [1, 2, 3, 4])

    def test_2(self):
        self.assertEqual(add_lists([], (1, 2)), [1, 2])

    def test_3(self):
        self.assertEqual(add_lists([1, 2], ()), [1, 2])

    def test_4(self):
        self.assertEqual(add_lists([], ()), [])

    def test_5(self):
        self.assertEqual(add_lists([10, 20], (30, 40)), [10, 20, 30, 40])

    def test_6(self):
        self.assertEqual(add_lists(["a"], ("b",)), ["a", "b"])

    def test_7(self):
        self.assertEqual(add_lists([1, "x"], ("y", 2)), [1, "x", "y", 2])

    def test_8(self):
        self.assertEqual(add_lists([[1]], ((2,),)), [[1], (2,)])

    def test_9(self):
        self.assertEqual(add_lists([5], (6,)), [5, 6])

    def test_10(self):
        self.assertEqual(add_lists([0], ()), [0])

    def test_11(self):
        self.assertEqual(add_lists([1], [2, 3]), [1, 2, 3])

    def test_12(self):
        self.assertEqual(add_lists([True], (False,)), [True, False])

    def test_13(self):
        result = add_lists([1], (2,))
        self.assertIsInstance(result, list)

    def test_14(self):
        big = list(range(1000))
        self.assertEqual(add_lists(big, (1000, 1001)), list(range(1002)))

    def test_15(self):
        a = [1]
        b = (2,)
        result = add_lists(a, b)
        self.assertEqual(a, [1])

