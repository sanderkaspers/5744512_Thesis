import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_003 import *

class TestVersion(unittest.TestCase):
    def test_positive_integers(self): self.assertEqual(find_Volume(2, 3, 4), 24)

    def test_mixed_int_float(self): self.assertAlmostEqual(find_Volume(2, 3.5, 4), 28.0)

    def test_all_floats(self): self.assertAlmostEqual(find_Volume(1.2, 3.4, 5.6), 22.848)

    def test_zero_dimension(self): self.assertEqual(find_Volume(0, 3, 4), 0)

    def test_all_zeros(self): self.assertEqual(find_Volume(0, 0, 0), 0)

    def test_negative_dimension(self): self.assertEqual(find_Volume(-2, 3, 4), -24)

    def test_large_dimensions(self): self.assertEqual(find_Volume(100000, 100000, 100000), 10**15)

    def test_all_ones(self): self.assertEqual(find_Volume(1, 1, 1), 1)

    def test_all_same_values(self): self.assertEqual(find_Volume(3, 3, 3), 27)

