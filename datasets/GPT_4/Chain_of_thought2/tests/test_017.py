import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_017 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(multiply(3, 4), 12)

    def test_mixed_sign_integers(self): self.assertEqual(multiply(5, -2), -10)

    def test_floats(self): self.assertEqual(multiply(2.5, 4.0), 10.0)

    def test_int_float(self): self.assertEqual(multiply(3, 2.5), 7.5)

    def test_zero_multiplication(self): self.assertEqual(multiply(0, 1000), 0)

    def test_boolean_inputs(self): self.assertEqual(multiply(True, False), 0)

    def test_scientific_notation(self): self.assertEqual(multiply(1e2, 2e1), 2000.0)

    def test_complex_numbers(self): self.assertEqual(multiply(1 + 2j, 3 + 4j), (1 + 2j) * (3 + 4j))

    def test_large_and_small(self): self.assertEqual(multiply(1e6, 1e-6), 1.0)

    def test_string_by_int(self): self.assertEqual(multiply("ab", 3), "ababab")

    def test_list_by_int(self): self.assertEqual(multiply([1], 3), [1, 1, 1])

