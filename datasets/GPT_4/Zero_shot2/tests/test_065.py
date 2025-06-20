import unittest
from datasets.GPT_4.Zero_shot2.programs.program_065 import *

class TestVersion(unittest.TestCase):
    def test_amicable_1(self):
        self.assertEqual(amicable_numbers_sum(300), 504)

    def test_amicable_2(self):
        self.assertEqual(amicable_numbers_sum(200), 220)

    def test_amicable_3(self):
        self.assertEqual(amicable_numbers_sum(1), 0)

    def test_amicable_4(self):
        self.assertEqual(amicable_numbers_sum(-10), 0)

    def test_amicable_5(self):
        self.assertEqual(amicable_numbers_sum("1000"), 0)

    def test_amicable_6(self):
        self.assertEqual(amicable_numbers_sum(10000), 31626)

    def test_amicable_7(self):
        self.assertEqual(amicable_numbers_sum(220), 0)

