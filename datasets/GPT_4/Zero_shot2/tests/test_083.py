import unittest
from datasets.GPT_4.Zero_shot2.programs.program_083 import *

class TestVersion(unittest.TestCase):
    def test_list_1(self):
        self.assertEqual(find_lists([[1], 2, 3]), [[1], [1]])

    def test_list_2(self):
        self.assertEqual(find_lists([[[]]]), [[[]], [[]], []])

    def test_list_3(self):
        self.assertEqual(find_lists([1, 2, 3]), [[1, 2, 3]])

    def test_list_4(self):
        self.assertEqual(find_lists([]), [[]])

    def test_list_5(self):
        self.assertEqual(find_lists(123), [])

    def test_list_6(self):
        self.assertEqual(find_lists([[[[[1]]]]]), [[[[[1]]]], [[[1]]], [[1]], [1]])

    def test_list_7(self):
        self.assertEqual(find_lists([1, [2]]), [[1, [2]]])

