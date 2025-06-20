import unittest
from datasets.GPT_4.Zero_shot2.programs.program_017 import *

class TestVersion(unittest.TestCase):
    def test_sum_1(self):
        self.assertEqual(recursive_list_sum([1, 2, 3]), 6)

    def test_sum_2(self):
        self.assertEqual(recursive_list_sum([1, [2, 3]]), 6)

    def test_sum_3(self):
        self.assertEqual(recursive_list_sum([1, [2, [3, [4]]]]), 10)

    def test_sum_4(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_sum_5(self):
        self.assertEqual(recursive_list_sum([[], [[], []]]), 0)

    def test_sum_6(self):
        self.assertEqual(recursive_list_sum([42]), 42)

    def test_sum_7(self):
        self.assertEqual(recursive_list_sum([[1], 2, [3, [4, [5]]]]), 15)

