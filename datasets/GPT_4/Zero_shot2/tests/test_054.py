import unittest
from datasets.GPT_4.Zero_shot2.programs.program_054 import *

class TestVersion(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(add_lists([1, 2], (3, 4)), [1, 2, 3, 4])

    def test_add_2(self):
        self.assertEqual(add_lists([1, 2], ()), [1, 2])

    def test_add_3(self):
        self.assertEqual(add_lists([], (3, 4)), [3, 4])

    def test_add_4(self):
        self.assertEqual(add_lists([], ()), [])

    def test_add_5(self):
        self.assertEqual(add_lists(['a', 1], ('b', 2)), ['a', 1, 'b', 2])

    def test_add_6(self):
        self.assertEqual(add_lists([1, [2]], ((3,),)), [1, [2], (3,)])

