import unittest
from datasets.GPT_4.Zero_shot1.programs.program_082 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_samepair([1,2,3],[4,5,6],[7,8,9]), 0)

    def test_2(self):
        self.assertEqual(count_samepair([1,2,3],[1,5,3],[1,8,3]), 2)

    def test_3(self):
        self.assertEqual(count_samepair([1,2],[1,2,3],[1,2,3]), 2)

    def test_4(self):
        self.assertEqual(count_samepair([],[],[]), 0)

    def test_5(self):
        self.assertEqual(count_samepair([5],[5],[5]), 1)

    def test_6(self):
        self.assertEqual(count_samepair([5],[5],[0]), 0)

    def test_7(self):
        self.assertEqual(count_samepair(['a', 2, True], ['a', 2, True], ['a', 2, True]), 3)

    def test_8(self):
        self.assertEqual(count_samepair([1,1,1],[1,2,1],[1,1,1]), 2)

    def test_9(self):
        self.assertEqual(count_samepair([[1],[2],[3]], [[1],[4],[3]], [[1],[2],[3]]), 1)

    def test_10(self):
        self.assertIsInstance(count_samepair([1],[1],[1]), int)

