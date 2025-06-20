import unittest
from datasets.GPT_4.Few_shot2.programs.program_079 import *

class TestVersion(unittest.TestCase):
    def test_circle_circumference_unit_circle(self): self.assertAlmostEqual(circle_circumference(1), 6.28318, places=5)

    def test_circle_circumference_zero_radius(self): self.assertEqual(circle_circumference(0), 0)

    def test_circle_circumference_large_radius(self): self.assertAlmostEqual(circle_circumference(100), 628.159, places=3)

    def test_circle_circumference_small_radius(self): self.assertAlmostEqual(circle_circumference(0.5), 3.14159, places=5)

    def test_circle_circumference_negative_radius(self): self.assertAlmostEqual(circle_circumference(-2), -12.56636, places=5)

