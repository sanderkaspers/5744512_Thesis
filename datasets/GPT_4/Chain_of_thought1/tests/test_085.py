import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_085 import *

class TestVersion(unittest.TestCase):
    def test_basic_case(self): self.assertEqual(find_solution(3, 5, 11), (2, 1))

    def test_multiple_solutions(self): self.assertEqual(find_solution(2, 4, 8), (0, 2))

    def test_valid_combination(self): self.assertEqual(find_solution(2, 3, 7), (2, 1))

    def test_a_b_are_1(self): self.assertEqual(find_solution(1, 1, 1), (0, 1))

    def test_no_solution(self): self.assertIsNone(find_solution(4, 6, 5))

    def test_zero_target(self): self.assertEqual(find_solution(1, 1, 0), (0, 0))

    def test_zero_a(self): self.assertEqual(find_solution(0, 5, 10), (0, 2))

    def test_zero_b(self): self.assertEqual(find_solution(5, 0, 10), (2, 0))

    def test_all_zero(self): self.assertEqual(find_solution(0, 0, 0), (0, 0))

    def test_unsolvable_all_zero(self): self.assertIsNone(find_solution(0, 0, 5))

    def test_negative_n(self): self.assertIsNone(find_solution(2, 3, -1))

    def test_negative_a(self): self.assertEqual(find_solution(-2, 3, 3), (0, 1))

    def test_negative_b(self): self.assertEqual(find_solution(3, -2, 3), (1, 0))

