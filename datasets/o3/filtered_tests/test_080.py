import unittest
from datasets.o3.programs.program_080 import *

class TestVersion(unittest.TestCase):
    def test_basic_duplicate_removal(self):
        data = [[1,2,3],[3,4,5],[5,6]]
        self.assertEqual(extract_singly(data), [1,2,3,4,5,6])

    def test_order_preserved(self):
        data = [['a','b'],['b','c'],['a','d']]
        self.assertEqual(extract_singly(data), ['a','b','c','d'])

    def test_empty_input_returns_empty(self):
        self.assertEqual(extract_singly([]), [])

    def test_inner_empty_lists(self):
        data = [[],[1,2],[],[2,3]]
        self.assertEqual(extract_singly(data), [1,2,3])

    def test_non_integer_elements(self):
        data = [[True, False],[False, None]]
        self.assertEqual(extract_singly(data), [True, False, None])

    def test_single_inner_list(self):
        data = [[7,8,7,9]]
        self.assertEqual(extract_singly(data), [7,8,9])

    def test_repeated_elements_in_same_inner(self):
        data = [[1,1,2],[2,2,3]]
        self.assertEqual(extract_singly(data), [1,2,3])

