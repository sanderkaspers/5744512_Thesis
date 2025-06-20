import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_009 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer(self): self.assertEqual(square(4), 16)

    def test_negative_integer(self): self.assertEqual(square(-5), 25)

    def test_zero(self): self.assertEqual(square(0), 0)

    def test_positive_float(self): self.assertEqual(square(2.5), 6.25)

    def test_negative_float(self): self.assertEqual(square(-1.5), 2.25)

    def test_large_number(self): self.assertEqual(square(1e6), 1e12)

    def test_small_float(self): self.assertAlmostEqual(square(1e-6), 1e-12)

    def test_boolean_true(self): self.assertEqual(square(True), 1)

    def test_boolean_false(self): self.assertEqual(square(False), 0)

    def test_scientific_notation(self): self.assertEqual(square(5e3), 25e6)

    def test_complex_number(self): self.assertEqual(square(1 + 2j), (1 + 2j) * (1 + 2j))

