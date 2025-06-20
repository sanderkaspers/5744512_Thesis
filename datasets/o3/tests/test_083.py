import unittest
from datasets.o3.programs.program_083 import *

class TestVersion(unittest.TestCase):
    def test_find_lists_non_empty_list(self):
        self.assertEqual(find_lists([1,2,3]), 1)

    def test_find_lists_empty_list(self):
        self.assertEqual(find_lists([]), 1)

    def test_find_lists_string(self):
        self.assertEqual(find_lists("abc"), 3)

    def test_find_lists_tuple(self):
        self.assertEqual(find_lists((1,2,3,4)), 4)

    def test_find_lists_dict(self):
        self.assertEqual(find_lists({'x':1,'y':2}), 2)

    def test_find_lists_list_of_lists(self):
        self.assertEqual(find_lists([[1],[2]]), 1)

    def test_find_lists_invalid_type(self):
        with self.assertRaises(TypeError):
            find_lists(42)

