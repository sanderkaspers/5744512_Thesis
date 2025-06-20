import unittest
from datasets.GPT_4.Few_shot1.programs.program_085 import *

class TestVersion(unittest.TestCase):
    def test_find_solution_basic(self): self.assertEqual(find_solution(3, 5, 11), (2, 1))

    def test_find_solution_exact_match(self): self.assertEqual(find_solution(2, 3, 12), (0, 4))

    def test_find_solution_zero_target(self): self.assertEqual(find_solution(4, 6, 0), (0, 0))

    def test_find_solution_no_solution(self): self.assertIsNone(find_solution(4, 6, 5))

    def test_find_solution_small_coefficients(self): self.assertEqual(find_solution(1, 1, 1), (1, 0))

    def test_find_solution_reversed_params(self): self.assertEqual(find_solution(5, 3, 11), (1, 2))

    def test_find_solution_same_coefficients(self): self.assertEqual(find_solution(2, 2, 8), (0, 4))

    def test_find_solution_large_n(self): self.assertEqual(find_solution(7, 11, 1001), (8, 77))

    def test_find_solution_edge_start(self): self.assertEqual(find_solution(5, 10, 10), (0, 1))

    def test_find_solution_bigger_first_coeff(self): self.assertEqual(find_solution(10, 3, 19), (1, 3))

    def test_find_solution_bigger_second_coeff(self): self.assertEqual(find_solution(3, 10, 19), (3, 1))

    def test_find_solution_large_coeffs(self): self.assertEqual(find_solution(20, 30, 150), (0, 5))

    def test_find_solution_multiple_valid(self): self.assertEqual(find_solution(2, 4, 10), (1, 2))

    def test_find_solution_negative_result(self): self.assertIsNone(find_solution(7, 5, 1))

    def test_find_solution_just_enough(self): self.assertEqual(find_solution(4, 6, 24), (0, 4))

