import unittest
from datasets.GPT_4.Few_shot2.programs.program_065 import *

class TestVersion(unittest.TestCase):
    def test_amicable_numbers_sum_limit_10(self): self.assertEqual(amicable_numbers_sum(10), 0)

    def test_amicable_numbers_sum_limit_300(self): self.assertEqual(amicable_numbers_sum(300), 504)

    def test_amicable_numbers_sum_limit_10000(self): self.assertEqual(amicable_numbers_sum(10000), 31626)

    def test_amicable_numbers_sum_no_amicables(self): self.assertEqual(amicable_numbers_sum(220), 0)

    def test_amicable_numbers_sum_min_valid(self): self.assertEqual(amicable_numbers_sum(2), 0)

