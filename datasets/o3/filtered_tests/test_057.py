import unittest
from datasets.o3.programs.program_057 import *

class TestVersion(unittest.TestCase):
    def test_common_numbers(self):
        nested=[[1,2,3],[2,3,4],[3,2]]
        self.assertEqual(sorted(common_in_nested_lists(nested)), [2,3])

    def test_no_common(self):
        nested=[[1,2],[3,4]]
        self.assertEqual(common_in_nested_lists(nested), [])

    def test_single_list(self):
        self.assertEqual(sorted(common_in_nested_lists([[1,1,2]])), [1,2])

    def test_duplicates_in_sublists(self):
        nested=[[1,1,2,3],[1,1,3,5]]
        self.assertEqual(sorted(common_in_nested_lists(nested)), [1,3])

    def test_empty_nestedlist(self):
        with self.assertRaises(TypeError):
            common_in_nested_lists([])

