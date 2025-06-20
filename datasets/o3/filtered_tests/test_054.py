import unittest
from datasets.o3.programs.program_054 import *

class TestVersion(unittest.TestCase):
    def test_basic_concat(self):
        self.assertEqual(add_lists([3,4], (1,2)), (1,2,3,4))

    def test_empty_list(self):
        self.assertEqual(add_lists([], (1,2)), (1,2))

    def test_empty_tuple(self):
        self.assertEqual(add_lists([1,2], ()), (1,2))

    def test_both_empty(self):
        self.assertEqual(add_lists([], ()), ())

    def test_immutability(self):
        lst = [5]
        tup = (6,)
        _ = add_lists(lst, tup)
        self.assertEqual(lst, [5])
        self.assertEqual(tup, (6,))

