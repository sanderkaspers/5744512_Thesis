import unittest
from datasets.GPT_4.Zero_shot2.programs.program_055 import *

class TestVersion(unittest.TestCase):
    def test_merge_1(self):
        self.assertEqual(merge_sorted_list([1,3], [2,4], 3), [1,2,3])

    def test_merge_2(self):
        self.assertEqual(merge_sorted_list([1,2], [3,4], 4), [1,2,3,4])

    def test_merge_3(self):
        self.assertEqual(merge_sorted_list([1], [2], 5), [1,2])

    def test_merge_4(self):
        self.assertEqual(merge_sorted_list([], [1,2,3], 2), [1,2])

    def test_merge_5(self):
        self.assertEqual(merge_sorted_list([], [], 3), [])

    def test_merge_6(self):
        self.assertEqual(merge_sorted_list([1,4], [2,4], 4), [1,2,4,4])

    def test_merge_7(self):
        self.assertEqual(merge_sorted_list([1,1,1], [1,1], 4), [1,1,1,1])

