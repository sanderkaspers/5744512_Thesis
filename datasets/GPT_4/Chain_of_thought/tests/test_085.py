import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_085 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_solution(3, 5, 11), (2, 1))

    def test_no_solution(self):
        self.assertEqual(find_solution(2, 4, 7), None)

    def test_a_zero(self):
        self.assertEqual(find_solution(0, 5, 10), (0, 2))

    def test_b_zero(self):
        self.assertEqual(find_solution(4, 0, 8), (2, 0))

    def test_n_zero(self):
        self.assertEqual(find_solution(3, 5, 0), (0, 0))

    def test_negative_n(self):
        self.assertEqual(find_solution(3, 5, -11), None)

    def test_large_values(self):
        self.assertEqual(find_solution(1000000, 500000, 1500000000), (1000, 1000))

    def test_negative_a(self):
        self.assertEqual(find_solution(-3, 5, 11), (-2, 1))

    def test_negative_b(self):
        self.assertEqual(find_solution(3, -5, 11), (2, -1))

    def test_a_equals_b(self):
        self.assertEqual(find_solution(5, 5, 10), (2, 0))

    def test_a_greater_than_n(self):
        self.assertEqual(find_solution(10, 2, 5), None)

    def test_b_greater_than_n(self):
        self.assertEqual(find_solution(2, 10, 5), None)

    def test_floating_point_inputs(self):
        self.assertEqual(find_solution(3.5, 5, 11), None)

