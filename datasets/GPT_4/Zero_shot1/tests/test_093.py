import unittest
from datasets.GPT_4.Zero_shot1.programs.program_093 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(frequency([1, 2, 3], 1), 1)

    def test_2(self):
        self.assertEqual(frequency([1, 2, 3], 4), 0)

    def test_3(self):
        self.assertEqual(frequency(["a", "b", "a"], "a"), 2)

    def test_4(self):
        self.assertEqual(frequency(["1", "2", "3"], 1), 0)

    def test_5(self):
        self.assertEqual(frequency([1, 2, 3], "1"), 0)

    def test_6(self):
        self.assertEqual(frequency(["A", "a", "A"], "a"), 1)

    def test_7(self):
        self.assertEqual(frequency([], 1), 0)

    def test_8(self):
        self.assertEqual(frequency([None, 1, None], None), 2)

    def test_9(self):
        self.assertEqual(frequency([1, "1", None], None), 1)

    def test_10(self):
        self.assertEqual(frequency([1, "1", 1.0], 1), 2)

    def test_11(self):
        self.assertIsInstance(frequency([1, 2, 3], 2), int)

