import unittest
from datasets.o3.programs.program_055 import *

class TestVersion(unittest.TestCase):
    def test_basic_merge(self):
        self.assertEqual(merge_sorted_list([3,1],[2],[5,4]), [1,2,3,4,5])

    def test_with_duplicates(self):
        self.assertEqual(merge_sorted_list([1,1],[1],[1]), [1,1,1,1])

    def test_with_negative_numbers(self):
        self.assertEqual(merge_sorted_list([-1,-3],[2,-2],[]), [-3,-2,-1,2])

    def test_all_empty(self):
        self.assertEqual(merge_sorted_list([],[],[]), [])

    def test_large_lists(self):
        a = list(range(100,0,-1))
        b = list(range(50,-50,-1))
        c = list(range(200,150,-1))
        res = merge_sorted_list(a,b,c)
        self.assertEqual(res, sorted(a+b+c))

