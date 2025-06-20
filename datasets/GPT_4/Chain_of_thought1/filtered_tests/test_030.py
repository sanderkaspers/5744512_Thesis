import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_030 import *

class TestVersion(unittest.TestCase):
    def test_zero_radius(self): self.assertEqual(volume_sphere(0), 0.0)

    def test_radius_one(self): self.assertAlmostEqual(volume_sphere(1), (4.0 / 3.0) * math.pi, places=6)

    def test_radius_two(self): self.assertAlmostEqual(volume_sphere(2), (4.0 / 3.0) * math.pi * 8, places=6)

    def test_large_radius(self): self.assertAlmostEqual(volume_sphere(1000), (4.0 / 3.0) * math.pi * 1000**3, places=2)

    def test_float_radius(self): self.assertAlmostEqual(volume_sphere(1.5), (4.0 / 3.0) * math.pi * (1.5 ** 3), places=6)

    def test_negative_radius(self): self.assertAlmostEqual(volume_sphere(-2), (4.0 / 3.0) * math.pi * (-2) ** 3, places=6)

    def test_string_input(self):
        with self.assertRaises(TypeError): volume_sphere('5')

    def test_none_input(self):
        with self.assertRaises(TypeError): volume_sphere(None)

    def test_list_input(self):
        with self.assertRaises(TypeError): volume_sphere([1])

