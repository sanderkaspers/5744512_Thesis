import unittest
from datasets.GPT_4.Zero_shot1.programs.program_045 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(frequency_lists([1, 2, 2, 3, 3, 3]), [(1, 1), (2, 2), (3, 3)])

    def test_2(self):
        self.assertEqual(frequency_lists(["a", "b", "a", "c", "c", "c"]), [("b", 1), ("a", 2), ("c", 3)])

    def test_3(self):
        self.assertEqual(frequency_lists([1, "1", 1, "1", "1"]), [(1, 2), ("1", 3)])

    def test_4(self):
        self.assertEqual(frequency_lists(["only"]), [("only", 1)])

    def test_5(self):
        self.assertEqual(frequency_lists([1, 2, 3]), [(1, 1), (2, 1), (3, 1)])

    def test_6(self):
        self.assertEqual(frequency_lists(["a", "a", "a"]), [("a", 3)])

    def test_7(self):
        self.assertEqual(frequency_lists([]), [])

    def test_8(self):
        self.assertEqual(frequency_lists([1, "1", 1]), [("1", 1), (1, 2)])

    def test_9(self):
        self.assertEqual(frequency_lists([4, 4, 2, 2, 1]), [(1, 1), (4, 2), (2, 2)])

    def test_10(self):
        result = frequency_lists(["x", "x", "y", "y", "z", "z"])
        self.assertEqual(set(result), {("x", 2), ("y", 2), ("z", 2)})

    def test_11(self):
        self.assertEqual(frequency_lists([1.1, 1.1, 2.2]), [(2.2, 1), (1.1, 2)])

    def test_12(self):
        self.assertEqual(frequency_lists([True, False, True]), [(False, 1), (True, 2)])

    def test_13(self):
        self.assertEqual(frequency_lists([None, None, 1]), [(1, 1), (None, 2)])

    def test_14(self):
        self.assertEqual(frequency_lists([-1, -1, -2]), [(-2, 1), (-1, 2)])

    def test_15(self):
        self.assertEqual(frequency_lists(["a", "b", "a", "b", "a"]), [("b", 2), ("a", 3)])

    def test_16(self):
        data = [1] * 10000 + [2] * 5000 + [3]
        result = frequency_lists(data)
        self.assertEqual(result, [(3, 1), (2, 5000), (1, 10000)])

