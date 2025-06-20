import unittest
from datasets.GPT_4.Zero_shot1.programs.program_007 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(test_duplicate([1, 2, 2, 3]), True)

    def test_2(self):
        self.assertEqual(test_duplicate([]), False)

    def test_3(self):
        self.assertEqual(test_duplicate([5]), False)

    def test_4(self):
        self.assertEqual(test_duplicate([0, 0, 0]), True)

    def test_5(self):
        self.assertEqual(test_duplicate([1, 2, 3, 4, 5, 5]), True)

    def test_6(self):
        self.assertEqual(test_duplicate([10, 20, 30, 10]), True)

    def test_7(self):
        self.assertEqual(test_duplicate([1.1, 2.2, 3.3, 1.1]), True)

    def test_9(self):
        self.assertEqual(test_duplicate(["a", "b", "c", "a"]), True)

    def test_9(self):
        self.assertEqual(test_duplicate(["x", "y", "z"]), False)

