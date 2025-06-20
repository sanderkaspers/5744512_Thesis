import unittest
from datasets.o3.programs.program_003 import *

class TestVersion(unittest.TestCase):
    def test_volume_integers(self):
        self.assertEqual(find_Volume(3,4,9), 36)

    def test_volume_floats(self):
        self.assertAlmostEqual(find_Volume(2.5,4.0,3.0), 10.0)

    def test_zero_dimension(self):
        self.assertEqual(find_Volume(0,5,7), 0)

    def test_negative_dimension(self):
        self.assertEqual(find_Volume(-3,2,1), -2.0)

    def test_large_numbers(self):
        self.assertEqual(find_Volume(1000,2000,3000), 2_000_000_000.0)

    def test_non_numeric_type_error(self):
        with self.assertRaises(TypeError):
            find_Volume("a",2,3)

