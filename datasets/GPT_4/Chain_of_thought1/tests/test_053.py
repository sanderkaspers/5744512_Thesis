import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_053 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(count([1, 2, 3, 4]), 10)

    def test_negative_integers(self): self.assertEqual(count([-1, -2, -3]), -6)

    def test_mixed_integers(self): self.assertEqual(count([-1, 0, 5, -3]), 1)

    def test_floats(self): self.assertAlmostEqual(count([1.5, 2.5, 3.0]), 7.0)

    def test_mixed_numbers(self): self.assertAlmostEqual(count([1, 2.5, 3]), 6.5)

    def test_empty_list(self): self.assertEqual(count([]), 0)

    def test_all_zeros(self): self.assertEqual(count([0, 0, 0]), 0)

    def test_single_element(self): self.assertEqual(count([42]), 42)

    def test_boolean_values(self): self.assertEqual(count([True, False, True]), 2)

