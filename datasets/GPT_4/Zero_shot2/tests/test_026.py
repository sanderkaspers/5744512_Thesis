import unittest
from datasets.GPT_4.Zero_shot2.programs.program_026 import *

class TestVersion(unittest.TestCase):
    def test_tuples_1(self):
        self.assertEqual(find_tuples([(1, 2), (3,), (4, 5, 6)], 2), [(1, 2)])

    def test_tuples_2(self):
        self.assertEqual(find_tuples([(1,), (2,), (3,)], 2), [])

    def test_tuples_3(self):
        self.assertEqual(find_tuples([(1, 2), (3, 4)], 2), [(1, 2), (3, 4)])

    def test_tuples_4(self):
        self.assertEqual(find_tuples([], 1), [])

    def test_tuples_5(self):
        self.assertEqual(find_tuples([(), (1,), (2, 3)], 0), [()])

    def test_tuples_6(self):
        self.assertEqual(find_tuples([(1,), (2,), (3,)], 0), [])

    def test_tuples_7(self):
        self.assertEqual(find_tuples([(1,), (2,)], 5), [])

    def test_tuples_8(self):
        self.assertEqual(find_tuples([((1,), (2,)), ((3, 4),)], 1), [((3, 4),)])

