import unittest
from datasets.o3.programs.program_085 import *

class TestVersion(unittest.TestCase):
    def test_find_solution_general_case(self):
        self.assertEqual(find_solution(3,5,11), (2,1))

    def test_find_solution_divisible_by_b(self):
        self.assertEqual(find_solution(3,5,20), (0,4))

    def test_find_solution_divisible_by_a(self):
        self.assertEqual(find_solution(4,6,12), (3,0))

    def test_find_solution_no_solution(self):
        self.assertIsNone(find_solution(4,6,7))

    def test_find_solution_zero_n(self):
        self.assertEqual(find_solution(4,6,0), (0,0))

    def test_find_solution_a_equals_one(self):
        self.assertEqual(find_solution(1,7,10), (10,0))

    def test_find_solution_large_numbers(self):
        self.assertEqual(find_solution(17,23,391), (8,5))

