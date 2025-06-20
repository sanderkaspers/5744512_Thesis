import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_003 import *

class TestVersion(unittest.TestCase):
    def test_integer_inputs(self): self.assertEqual(find_Volume(3, 4, 6), 24.0)

    def test_float_inputs(self): self.assertAlmostEqual(find_Volume(2.5, 3.2, 4.1), (2.5 * 3.2 * 4.1) / 3)

    def test_zero_length(self): self.assertEqual(find_Volume(0, 3, 4), 0.0)

    def test_zero_breadth(self): self.assertEqual(find_Volume(3, 0, 4), 0.0)

    def test_zero_height(self): self.assertEqual(find_Volume(3, 4, 0), 0.0)

    def test_cube_base(self): self.assertEqual(find_Volume(5, 5, 5), (5 * 5 * 5) / 3)

    def test_negative_length(self): self.assertEqual(find_Volume(-3, 4, 5), (-3 * 4 * 5) / 3)

    def test_negative_height(self): self.assertEqual(find_Volume(3, 4, -5), (3 * 4 * -5) / 3)

    def test_large_values(self): self.assertEqual(find_Volume(1e6, 1e6, 1e6), (1e6 * 1e6 * 1e6) / 3)

    def test_small_values(self): self.assertAlmostEqual(find_Volume(1e-6, 1e-6, 1e-6), (1e-6 * 1e-6 * 1e-6) / 3)

    def test_mixed_types(self): self.assertAlmostEqual(find_Volume(5, 2.5, 3), (5 * 2.5 * 3) / 3)

    def test_scientific_notation(self): self.assertEqual(find_Volume(1e3, 2e3, 3e3), (1e3 * 2e3 * 3e3) / 3)

