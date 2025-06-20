import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_005 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer(self): self.assertEqual(square_perimeter(5), 20)

    def test_positive_float(self): self.assertEqual(square_perimeter(2.5), 10.0)

    def test_zero_input(self): self.assertEqual(square_perimeter(0), 0)

    def test_negative_input(self): self.assertEqual(square_perimeter(-3), -12)

    def test_large_input(self): self.assertEqual(square_perimeter(1e6), 4e6)

    def test_small_float(self): self.assertEqual(square_perimeter(1e-6), 4e-6)

    def test_boolean_true(self): self.assertEqual(square_perimeter(True), 4)

    def test_boolean_false(self): self.assertEqual(square_perimeter(False), 0)

    def test_scientific_notation(self): self.assertEqual(square_perimeter(5e2), 2000.0)

