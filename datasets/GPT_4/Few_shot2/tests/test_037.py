import unittest
from datasets.GPT_4.Few_shot2.programs.program_037 import *

class TestVersion(unittest.TestCase):
    def test_closest_num_positive(self): self.assertEqual(closest_num(10), 9)

    def test_closest_num_zero(self): self.assertEqual(closest_num(0), -1)

    def test_closest_num_negative(self): self.assertEqual(closest_num(-5), -6)

    def test_closest_num_one(self): self.assertEqual(closest_num(1), 0)

    def test_closest_num_large_number(self): self.assertEqual(closest_num(1000000), 999999)

    def test_closest_num_float(self): self.assertEqual(closest_num(3.5), 2.5)

    def test_closest_num_negative_float(self): self.assertEqual(closest_num(-2.5), -3.5)

    def test_closest_num_small_float(self): self.assertEqual(closest_num(0.1), -0.9)

    def test_closest_num_boolean_true(self): self.assertEqual(closest_num(True), 0)

    def test_closest_num_boolean_false(self): self.assertEqual(closest_num(False), -1)

