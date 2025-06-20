import unittest
from datasets.o3.programs.program_082 import *

class TestVersion(unittest.TestCase):
    def test_count_samepair_all_equal(self):
        self.assertEqual(count_samepair([1,1],[1,1],[1,1]), 2)

    def test_count_samepair_none_equal(self):
        self.assertEqual(count_samepair([1,2],[2,3],[3,4]), 0)

    def test_count_samepair_some_equal(self):
        self.assertEqual(count_samepair([1,2,3],[1,4,3],[1,2,3]), 2)

    def test_count_samepair_different_lengths(self):
        self.assertEqual(count_samepair([1,2,3,4],[1,2,3],[1,2,3,4,5]), 3)

    def test_count_samepair_empty_lists(self):
        self.assertEqual(count_samepair([],[],[]), 0)

    def test_count_samepair_strings(self):
        self.assertEqual(count_samepair(['a','b'],['a','x'],['a','b']), 1)

    def test_count_samepair_single_element(self):
        self.assertEqual(count_samepair([7],[7],[7]), 1)

