import unittest
from datasets.GPT_4.Zero_shot1.programs.program_065 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(amicable_numbers_sum(300), 220)

    def test_2(self):
        self.assertEqual(amicable_numbers_sum(0), 0)

    def test_3(self):
        self.assertEqual(amicable_numbers_sum(1), 0)

    def test_4(self):
        self.assertEqual(amicable_numbers_sum("100"), 0)

    def test_5(self):
        self.assertEqual(amicable_numbers_sum(-50), 0)

