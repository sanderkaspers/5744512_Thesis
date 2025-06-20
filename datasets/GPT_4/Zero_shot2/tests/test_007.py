import unittest
from datasets.GPT_4.Zero_shot2.programs.program_007 import *

class TestVersion(unittest.TestCase):
    def test_duplicate_1(self):
        self.assertFalse(test_duplicate([1, 2, 3, 4]))

    def test_duplicate_2(self):
        self.assertTrue(test_duplicate([1, 2, 3, 1]))

    def test_duplicate_3(self):
        self.assertTrue(test_duplicate([5, 5, 5, 5]))

    def test_duplicate_4(self):
        self.assertFalse(test_duplicate([]))

    def test_duplicate_5(self):
        self.assertTrue(test_duplicate(["a", "b", "a"]))

    def test_duplicate_6(self):
        self.assertTrue(test_duplicate(list(range(100000)) + [99999]))

