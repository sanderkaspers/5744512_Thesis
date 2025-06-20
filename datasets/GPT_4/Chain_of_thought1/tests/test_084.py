import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_084 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(max_Abs_Diff([1, 2, 3]), 2)

    def test_negative_integers(self): self.assertEqual(max_Abs_Diff([-1, -2, -3]), 2)

    def test_mixed_signs(self): self.assertEqual(max_Abs_Diff([-10, 0, 5]), 15)

    def test_single_element(self): self.assertEqual(max_Abs_Diff([7]), 0)

    def test_same_elements(self): self.assertEqual(max_Abs_Diff([4, 4, 4]), 0)

    def test_large_range(self): self.assertEqual(max_Abs_Diff([100, -1000, 500]), 1500)

    def test_floats(self): self.assertAlmostEqual(max_Abs_Diff([1.1, 2.5, -3.6]), 6.1, places=2)

    def test_boolean_values(self): self.assertEqual(max_Abs_Diff([True, False, True]), 1)

