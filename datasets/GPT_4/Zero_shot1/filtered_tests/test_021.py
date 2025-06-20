import unittest
from datasets.GPT_4.Zero_shot1.programs.program_021 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_sublist([1, 2, 3, 4], [3, 5]), False)

    def test_2(self):
        self.assertEqual(is_sublist([1, 2, 3], [1, 2]), True)

    def test_3(self):
        self.assertEqual(is_sublist([1, 2, 3], [2, 3]), True)

    def test_4(self):
        self.assertEqual(is_sublist([1, 2, 3], [1, 2, 3]), True)

    def test_5(self):
        self.assertEqual(is_sublist([1, 2, 3], []), True)

    def test_6(self):
        self.assertEqual(is_sublist([1, 2], [1, 2, 3]), False)

    def test_7(self):
        self.assertEqual(is_sublist([1, 2, 2, 3], [2, 2]), True)

    def test_8(self):
        self.assertEqual(is_sublist([1, 2, 2, 3], [2, 3]), True)

