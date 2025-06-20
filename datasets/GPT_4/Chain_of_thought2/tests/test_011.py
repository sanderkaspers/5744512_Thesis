import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_011 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(average_of_three(3, 6, 9), 6.0)

    def test_negative_integers(self): self.assertEqual(average_of_three(-3, -6, -9), -6.0)

    def test_mixed_signs(self): self.assertEqual(average_of_three(-3, 0, 3), 0.0)

    def test_float_inputs(self): self.assertEqual(average_of_three(1.5, 2.5, 3.5), 2.5)

    def test_mixed_types(self): self.assertEqual(average_of_three(1, 2.0, 3), 2.0)

    def test_all_zeros(self): self.assertEqual(average_of_three(0, 0, 0), 0.0)

    def test_booleans(self): self.assertEqual(average_of_three(True, False, True), 2 / 3)

    def test_large_numbers(self): self.assertEqual(average_of_three(1e9, 1e9, 1e9), 1e9)

    def test_small_floats(self): self.assertAlmostEqual(average_of_three(1e-9, 2e-9, 3e-9), 2e-9)

    def test_scientific_notation(self): self.assertEqual(average_of_three(1e2, 2e2, 3e2), 200.0)

    def test_complex_inputs(self): self.assertEqual(average_of_three(1+1j, 2+2j, 3+3j), 2+2j)

