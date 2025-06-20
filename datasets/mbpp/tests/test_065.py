import unittest
from datasets.mbpp.programs.program_065 import *

class TestVersion(unittest.TestCase):
    def test_amicable_numbers_sum_with_999_expect_504(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

    def test_amicable_numbers_sum_with_9999_expect_31626(self):
        self.assertEqual(amicable_numbers_sum(9999), 31626)

    def test_amicable_numbers_sum_with_99_expect_0(self):
        self.assertEqual(amicable_numbers_sum(99), 0)

