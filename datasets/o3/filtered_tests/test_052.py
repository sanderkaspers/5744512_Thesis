import unittest
from datasets.o3.programs.program_052 import *

class TestVersion(unittest.TestCase):
    def test_single_sublist(self):
        self.assertEqual(sort_sublists([[ (2,'b'), (1,'a') ]]), [[ (1,'a'), (2,'b') ]])

    def test_multiple_sublists(self):
        data = [[(3, 'c'), (1, 'a')], [(2, 'b'), (2, 'a')]]
        expected = [[(1, 'a'), (3, 'c')], [(2, 'b'), (2, 'a')]]
        self.assertEqual(sort_sublists(data), expected)

    def test_empty_input(self):
        self.assertEqual(sort_sublists([]), [])

    def test_sublist_with_single_element(self):
        self.assertEqual(sort_sublists([[ (5,'x') ]]), [[ (5,'x') ]])

    def test_duplicate_first_elements(self):
        data = [[(1, 'a'), (1, 'b'), (0, 'c')]]
        expected = [[(0, 'c'), (1, 'a'), (1, 'b')]]
        self.assertEqual(sort_sublists(data), expected)

