import unittest
from datasets.GPT_4.Zero_shot1.programs.program_057 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sorted(common_in_nested_lists([[1, 2, 3], [2, 3], [3, 2]])), [2, 3])

    def test_2(self):
        self.assertEqual(common_in_nested_lists([[1, 2], [3, 4]]), [])

    def test_3(self):
        self.assertEqual(sorted(common_in_nested_lists([[1, 2, 3]])), [1, 2, 3])

    def test_4(self):
        self.assertEqual(common_in_nested_lists([[1, 2], [], [1]]), [])

    def test_5(self):
        self.assertEqual(common_in_nested_lists([[], [], []]), [])

    def test_6(self):
        self.assertEqual(sorted(common_in_nested_lists([[1, 1, 2], [1, 2, 2], [1]])), [1])

    def test_7(self):
        self.assertEqual(common_in_nested_lists([[5, 6, 7], [7, 8, 9], [7]]), [7])

    def test_8(self):
        result = common_in_nested_lists([[1, 2], [2, 3]])
        self.assertIsInstance(result, list)

