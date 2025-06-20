import unittest
from datasets.GPT_4.Zero_shot1.programs.program_026 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_tuples([(1, 3), (3, 5), (5, 7)], 1), [])

    def test_2(self):
        self.assertEqual(find_tuples([(2, 1), (4, 3), (6, 5)], 0), [(2, 1), (4, 3), (6, 5)])

    def test_3(self):
        self.assertEqual(find_tuples([(2, 3), (4, 5), (7, 8)], 1), [(7, 8)])

    def test_4(self):
        self.assertEqual(find_tuples([], 0), [])

    def test_5(self):
        self.assertEqual(find_tuples([(1, -2), (3, -4)], 1), [(1, -2), (3, -4)])

