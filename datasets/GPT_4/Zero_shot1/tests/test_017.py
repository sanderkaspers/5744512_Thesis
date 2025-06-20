import unittest
from datasets.GPT_4.Zero_shot1.programs.program_017 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(recursive_list_sum([1, [2, 3]]), 6)

    def test_2(self):
        self.assertEqual(recursive_list_sum([1, [2, [3, 4]], 5]), 15)

    def test_3(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_4(self):
        self.assertEqual(recursive_list_sum([[], [], []]), 0)

    def test_5(self):
        self.assertEqual(recursive_list_sum([10]), 10)

    def test_6(self):
        self.assertEqual(recursive_list_sum([-1, [0, [2]]]), 1)

    def test_7(self):
        self.assertEqual(recursive_list_sum([[1], [[2], [[3]]]]), 6)

    def test_8(self):
        self.assertEqual(recursive_list_sum([[[[[[[[4]]]]]]]]), 4)

