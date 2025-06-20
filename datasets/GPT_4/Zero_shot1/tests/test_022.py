import unittest
from datasets.GPT_4.Zero_shot1.programs.program_022 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_equal_tuple([(1, 1), (2, 2)]), [(1, 1), (2, 2)])

    def test_2(self):
        self.assertEqual(find_equal_tuple([(1, 2), (3, 3)]), [(3, 3)])

    def test_3(self):
        self.assertEqual(find_equal_tuple([(1, 2), (3, 4)]), [])

    def test_4(self):
        self.assertEqual(find_equal_tuple([(1,), (2,), (2, 2)]), [(1,), (2,), (2, 2)])

    def test_5(self):
        self.assertEqual(find_equal_tuple([("a", "a"), ("b", "c")]), [("a", "a")])

    def test_6(self):
        self.assertEqual(find_equal_tuple([(1.1, 1.1), (2.2, 2.3)]), [(1.1, 1.1)])

    def test_7(self):
        self.assertEqual(find_equal_tuple([(0, 0), (0, 0), (1, 2)]), [(0, 0), (0, 0)])

