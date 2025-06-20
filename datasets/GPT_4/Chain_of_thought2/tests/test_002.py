import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_002 import *

class TestVersion(unittest.TestCase):
    def test_distinct_sums(self): M=[[3,4],[1,2,3],[5]]; expected=[[5],[3,4],[1,2,3]]; self.assertEqual(sort_matrix(M), expected)

    def test_identical_sums(self): M=[[2,2],[1,3],[4,0]]; expected=[[2,2],[1,3],[4,0]]; self.assertEqual(sort_matrix(M), expected)

    def test_single_row(self): M=[[10,20,30]]; expected=[[10,20,30]]; self.assertEqual(sort_matrix(M), expected)

    def test_one_column(self): M=[[3],[1],[2]]; expected=[[1],[2],[3]]; self.assertEqual(sort_matrix(M), expected)

    def test_already_sorted(self): M=[[1],[2,1],[2,2]]; expected=[[1],[2,1],[2,2]]; self.assertEqual(sort_matrix(M), expected)

    def test_empty_matrix(self): M=[]; expected=[]; self.assertEqual(sort_matrix(M), expected)

    def test_matrix_with_empty_rows(self): M=[[],[1,2],[],[3]]; expected=[[],[],[3],[1,2]]; self.assertEqual(sort_matrix(M), expected)

    def test_negative_numbers(self): M=[[-1,-2],[0],[-3,1]]; expected=[[-3,1],[-1,-2],[0]]; self.assertEqual(sort_matrix(M), expected)

    def test_floats(self): M=[[1.5,2.5],[2.0],[1.0,1.0,1.0]]; expected=[[2.0],[1.0,1.0,1.0],[1.5,2.5]]; self.assertEqual(sort_matrix(M), expected)

    def test_uneven_rows(self): M=[[1],[1,1],[1,1,1]]; expected=[[1],[1,1],[1,1,1]]; self.assertEqual(sort_matrix(M), expected)

    def test_large_matrix(self): M=[[i for i in range(100)] for _ in range(100)]; expected=M; self.assertEqual(sort_matrix(M), expected)

