import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_037 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer(self): self.assertEqual(closest_num(10), 9)

    def test_one(self): self.assertEqual(closest_num(1), 0)

    def test_zero(self): self.assertEqual(closest_num(0), -1)

    def test_negative_integer(self): self.assertEqual(closest_num(-5), -6)

    def test_positive_float(self): self.assertEqual(closest_num(10.5), 9.5)

    def test_large_integer(self): self.assertEqual(closest_num(1000000), 999999)

    def test_small_negative_float(self): self.assertAlmostEqual(closest_num(-0.000001), -1.000001)

    def test_boolean_true(self): self.assertEqual(closest_num(True), 0)

    def test_boolean_false(self): self.assertEqual(closest_num(False), -1)

