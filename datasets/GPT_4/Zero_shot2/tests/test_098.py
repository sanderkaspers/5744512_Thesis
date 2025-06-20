import unittest
from datasets.GPT_4.Zero_shot2.programs.program_098 import *

class TestVersion(unittest.TestCase):
    def test_majority_1(self):
        self.assertTrue(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3))

    def test_majority_2(self):
        self.assertFalse(is_majority([1, 1, 2, 4, 4, 4, 6], 7, 4))

    def test_majority_3(self):
        self.assertFalse(is_majority([1, 1, 2, 2, 3], 5, 4))

    def test_majority_4(self):
        self.assertTrue(is_majority([5], 1, 5))

    def test_majority_5(self):
        self.assertFalse(is_majority([6], 1, 5))

    def test_majority_6(self):
        self.assertTrue(is_majority([2, 2, 2, 2], 4, 2))

    def test_majority_7(self):
        self.assertFalse(is_majority([2, 2, 2, 3, 3, 3], 6, 2))

    def test_majority_8(self):
        self.assertFalse(is_majority([1, 2, 2, 2, 3], 5, 2))

    def test_majority_9(self):
        self.assertTrue(is_majority([1, 2, 2, 2, 2], 5, 2))

    def test_majority_10(self):
        self.assertFalse(is_majority([], 0, 1))

