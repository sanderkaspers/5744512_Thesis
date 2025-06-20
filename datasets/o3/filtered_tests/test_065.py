import unittest
from datasets.o3.programs.program_065 import *

class TestVersion(unittest.TestCase):
    def test_non_integer_input(self):
        self.assertEqual(amicable_numbers_sum(5.5), "Input is not an integer!")

    def test_negative_input(self):
        self.assertEqual(amicable_numbers_sum(-10), "Input must be bigger than 0!")

    def test_zero_input(self):
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")

    def test_no_amicables_under_100(self):
        self.assertEqual(amicable_numbers_sum(100), 0)

    def test_first_pair_partial(self):
        # only 220 counts when limit is 220 because 284 is out of range
        self.assertEqual(amicable_numbers_sum(220), 220)

    def test_first_pair_full(self):
        self.assertEqual(amicable_numbers_sum(284), 504)

    def test_sum_up_to_10000(self):
        self.assertEqual(amicable_numbers_sum(10000), 31626)

