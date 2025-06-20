import unittest
from datasets.GPT_4.Zero_shot2.programs.program_057 import *

class TestVersion(unittest.TestCase):
    def test_common_1(self):
        self.assertEqual(sorted(common_in_nested_lists([[1,2,3],[2,3,4],[2,5]])), [2])

    def test_common_2(self):
        self.assertEqual(common_in_nested_lists([[1,2],[3,4]]), [])

    def test_common_3(self):
        self.assertEqual(sorted(common_in_nested_lists([[5,5,5]])), [5])

    def test_common_4(self):
        self.assertEqual(common_in_nested_lists([[1,2],[]]), [])

    def test_common_5(self):
        self.assertEqual(common_in_nested_lists([[1,2,2],[2,2,3]]), [2])

    def test_common_6(self):
        self.assertEqual(sorted(common_in_nested_lists([['a','b','c'],['b','c','d'],['b']])), ['b'])

