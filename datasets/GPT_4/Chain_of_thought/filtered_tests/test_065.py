import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_065 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(amicable_numbers_sum(1000), 504)

    def test_no_amicable_numbers(self):
        self.assertEqual(amicable_numbers_sum(200), 0)

    def test_limit_as_one(self):
        self.assertEqual(amicable_numbers_sum(1), 0)

    def test_non_integer_input(self):
        self.assertEqual(amicable_numbers_sum('1000'), 'Input is not an integer!')

    def test_negative_limit(self):
        self.assertEqual(amicable_numbers_sum(-100), 'Input must be bigger than 0!')

    def test_large_limit(self):
        self.assertGreater(amicable_numbers_sum(10000), 0)

    def test_floating_point_input(self):
        self.assertEqual(amicable_numbers_sum(1000.0), 'Input is not an integer!')

    def test_amicable_numbers_at_boundary(self):
        self.assertEqual(amicable_numbers_sum(284), 504)

    def test_very_large_amicable_numbers(self):
        self.assertGreater(amicable_numbers_sum(10000), 0)

    def test_string_input_as_number(self):
        self.assertEqual(amicable_numbers_sum('1000'), 'Input is not an integer!')

