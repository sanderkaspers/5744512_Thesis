import unittest
from datasets.GPT_4.Zero_shot2.programs.program_082 import *

class TestVersion(unittest.TestCase):
    def test_pair_1(self):
        self.assertEqual(count_samepair([1, 2], [1, 2], [1, 2]), 2)

    def test_pair_2(self):
        self.assertEqual(count_samepair([1, 2], [2, 1], [3, 4]), 0)

    def test_pair_3(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 5, 3], [1, 5, 4]), 1)

    def test_pair_4(self):
        self.assertEqual(count_samepair([], [], []), 0)

    def test_pair_5(self):
        self.assertEqual(count_samepair([7], [7], [7]), 1)

    def test_pair_6(self):
        self.assertEqual(count_samepair([1, 2], [1], [1, 2, 3]), 1)

    def test_pair_7(self):
        self.assertEqual(count_samepair(['a', 2], ['a', '2'], ['a', 2]), 1)

    def test_pair_8(self):
        self.assertEqual(count_samepair([-1, -2, -3], [-1, -2, 0], [-1, 0, -3]), 1)

    def test_pair_9(self):
        self.assertEqual(count_samepair([1, 1, 1], [1, 2, 1], [1, 2, 3]), 1)

    def test_pair_10(self):
        self.assertEqual(count_samepair(list(range(100)), list(range(100)), list(range(100))), 100)

