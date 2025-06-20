import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_021 import *

class TestVersion(unittest.TestCase):
    def test_positive_integer(self): self.assertEqual(square(5), 25)

    def test_negative_integer(self): self.assertEqual(square(-3), 9)

    def test_zero(self): self.assertEqual(square(0), 0)

    def test_positive_float(self): self.assertEqual(square(2.5), 6.25)

    def test_negative_float(self): self.assertEqual(square(-1.5), 2.25)

    def test_boolean_true(self): self.assertEqual(square(True), 1)

    def test_boolean_false(self): self.assertEqual(square(False), 0)

    def test_scientific_notation(self): self.assertEqual(square(1e2), 10000.0)

    def test_complex_number(self): self.assertEqual(square(2 + 3j), (2 + 3j) * (2 + 3j))

