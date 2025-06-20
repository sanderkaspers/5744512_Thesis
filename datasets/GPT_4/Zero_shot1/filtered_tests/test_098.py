import unittest
from datasets.GPT_4.Zero_shot1.programs.program_098 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertFalse(is_majority([1, 2, 3, 3, 3, 10], 6, 3))

    def test_2(self):
        self.assertFalse(is_majority([1, 2, 3, 4, 5], 5, 6))

    def test_3(self):
        self.assertFalse(is_majority([1, 2, 2, 3], 4, 2))

    def test_4(self):
        self.assertFalse(is_majority([2, 3, 4, 5, 6], 5, 2))

    def test_5(self):
        self.assertFalse(is_majority([1, 2, 3, 4, 5], 5, 5))

    def test_6(self):
        self.assertFalse(is_majority([], 0, 1))

    def test_7(self):
        self.assertTrue(is_majority([5], 1, 5))

    def test_8(self):
        self.assertFalse(is_majority([5], 1, 4))

    def test_9(self):
        self.assertTrue(is_majority([3]*501 + [4]*499, 1000, 3))

    def test_10(self):
        self.assertTrue(is_majority([1, 2, 3, 3, 3], 5, 3))

    def test_11(self):
        self.assertTrue(is_majority([4, 4, 4, 4], 4, 4))

    def test_12(self):
        self.assertFalse(is_majority([7, 8, 9, 10, 11], 5, 10))

    def test_13(self):
        self.assertEqual(binary_search([1, 2, 3, 4], 0, 3, 2), 1)

    def test_14(self):
        self.assertIsInstance(is_majority([1, 1, 1], 3, 1), bool)

