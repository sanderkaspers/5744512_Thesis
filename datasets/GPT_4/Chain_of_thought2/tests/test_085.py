import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_085 import *

class TestVersion(unittest.TestCase):
    def test_simple_solution_exists(self): self.assertEqual(find_solution(2, 3, 7), (2, 1))

    def test_no_solution_exists(self): self.assertIsNone(find_solution(4, 6, 7))

    def test_solution_at_x_zero(self): self.assertEqual(find_solution(4, 5, 10), (0, 2))

    def test_solution_at_x_one(self): self.assertEqual(find_solution(4, 3, 10), (1, 2))

    def test_a_or_b_larger_than_n(self): self.assertEqual(find_solution(15, 3, 18), (1, 1))

    def test_b_larger_than_n(self): self.assertEqual(find_solution(2, 20, 22), (1, 1))

    def test_zero_coefficients(self): self.assertEqual(find_solution(0, 5, 10), (0, 2))

    def test_zero_rhs(self): self.assertEqual(find_solution(2, 3, 0), (0, 0))

    def test_large_numbers(self): self.assertEqual(find_solution(5, 7, 100), (1, 13))

    def test_no_solution_due_to_modulo(self): self.assertIsNone(find_solution(6, 10, 1))

    def test_negative_n(self): self.assertIsNone(find_solution(2, 3, -1))

    def test_negative_a_or_b(self): self.assertEqual(find_solution(-2, 3, 4), (0, 1))

