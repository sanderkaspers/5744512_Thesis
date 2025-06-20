import unittest
from datasets.o3.programs.program_026 import *

class TestVersion(unittest.TestCase):
    def test_typical_match(self):
        data = [(1,2,3), (1,1,2), (4,5,6)]
        self.assertEqual(find_tuples(data, 3), [(1,2,3), (4,5,6)])

    def test_duplicates_filtered(self):
        data = [(1,1,1), (2,2), (1,2)]
        self.assertEqual(find_tuples(data, 2), [(1,2)])

    def test_empty_input(self):
        self.assertEqual(find_tuples([], 1), [])

    def test_k_greater_than_tuple_len(self):
        data = [(1,), (1,2)]
        self.assertEqual(find_tuples(data, 3), [])

    def test_empty_tuple_k_zero(self):
        data = [()]
        self.assertEqual(find_tuples(data, 0), [()])

