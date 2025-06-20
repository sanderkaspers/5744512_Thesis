import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_016 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(subtract(10, 4), 6)

    def test_mixed_sign_integers(self): self.assertEqual(subtract(5, -3), 8)

    def test_floats(self): self.assertEqual(subtract(5.5, 2.5), 3.0)

    def test_int_float(self): self.assertEqual(subtract(7, 2.5), 4.5)

    def test_zero(self): self.assertEqual(subtract(0, 0), 0)

    def test_large_and_small(self): self.assertEqual(subtract(1e6, 1e-6), 1e6 - 1e-6)

    def test_boolean_inputs(self): self.assertEqual(subtract(True, False), 1)

    def test_scientific_notation(self): self.assertEqual(subtract(1e2, 5e1), 50.0)

    def test_complex_numbers(self): self.assertEqual(subtract(3 + 4j, 1 + 2j), 2 + 2j)

