import unittest
from datasets.GPT_4.Few_shot1.programs.program_079 import *

class TestVersion(unittest.TestCase):
    def test_circle_circumference_unit(self): self.assertAlmostEqual(circle_circumference(1), 6.283)

    def test_circle_circumference_zero(self): self.assertAlmostEqual(circle_circumference(0), 0.0)

    def test_circle_circumference_small_radius(self): self.assertAlmostEqual(circle_circumference(0.5), 3.1415)

    def test_circle_circumference_large_radius(self): self.assertAlmostEqual(circle_circumference(1000), 6283.0)

    def test_circle_circumference_negative_radius(self): self.assertAlmostEqual(circle_circumference(-1), -6.283)

    def test_circle_circumference_float_precision(self): self.assertAlmostEqual(circle_circumference(1.234), 2 * 3.1415 * 1.234)

    def test_circle_circumference_int_input(self): self.assertAlmostEqual(circle_circumference(10), 62.83)

    def test_circle_circumference_float_input(self): self.assertAlmostEqual(circle_circumference(2.5), 15.7075)

    def test_circle_circumference_rounding_check(self): self.assertAlmostEqual(round(circle_circumference(2), 2), 12.57)

    def test_circle_circumference_expression_input(self): self.assertAlmostEqual(circle_circumference(2 + 3), 31.415)

