import unittest
from datasets.GPT_4.Zero_shot2.programs.program_021 import *

class TestVersion(unittest.TestCase):
    def test_sub_1(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [2, 3]))

    def test_sub_2(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3]))

    def test_sub_3(self):
        self.assertTrue(is_sublist([1, 2, 3], []))

    def test_sub_4(self):
        self.assertFalse(is_sublist([1, 2], [1, 2, 3]))

    def test_sub_5(self):
        self.assertFalse(is_sublist([1, 2, 3], [3, 4]))

    def test_sub_6(self):
        self.assertTrue(is_sublist([1, 2, 3], [1]))

    def test_sub_7(self):
        self.assertTrue(is_sublist([1, 2, 3], [3]))

    def test_sub_8(self):
        self.assertTrue(is_sublist([], []))

