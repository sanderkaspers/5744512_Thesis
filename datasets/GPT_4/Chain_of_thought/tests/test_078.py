import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_078 import *

class TestVersion(unittest.TestCase):
    def test_valid_sum_of_powers_of_two(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(3), True)

    def test_odd_number_not_representable(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(5), False)

    def test_even_number_representable(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(6), True)

    def test_even_number_not_representable(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True)

    def test_edge_case_n_equals_1(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(1), False)

    def test_large_number(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(2**20 + 2**10 + 1), True)

    def test_negative_number(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(-5), False)

    def test_zero_as_input(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(0), False)

    def test_prime_number(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(7), False)

    def test_perfect_power_of_two(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(16), True)

