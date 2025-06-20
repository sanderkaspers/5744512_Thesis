import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_027 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer(self): self.assertEqual(square_root(16), 4.0)

    def test_zero(self): self.assertEqual(square_root(0), 0.0)

    def test_positive_float(self): self.assertEqual(square_root(2.25), 1.5)

    def test_boolean_true(self): self.assertEqual(square_root(True), 1.0)

    def test_boolean_false(self): self.assertEqual(square_root(False), 0.0)

    def test_small_float(self): self.assertAlmostEqual(square_root(1e-10), 1e-5)

    def test_large_number(self): self.assertEqual(square_root(10**8), 10000.0)

    def test_negative_float(self): self.assertEqual(square_root(-4.0), (-4.0) ** 0.5)

    def test_negative_integer(self): self.assertEqual(square_root(-9), (-9) ** 0.5)

