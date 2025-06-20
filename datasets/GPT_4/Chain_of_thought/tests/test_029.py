import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_029 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tetrahedral_number(5), 35.0)  # 5th tetrahedral number

    def test_zero_input(self):
        self.assertEqual(tetrahedral_number(0), 0.0)  # 0th tetrahedral number

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            tetrahedral_number(-3)

    def test_large_number(self):
        self.assertEqual(tetrahedral_number(1000), 167167000.0)  # 1000th tetrahedral number

    def test_floating_point_input(self):
        with self.assertRaises(TypeError):
            tetrahedral_number(5.5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            tetrahedral_number('10')

    def test_max_integer(self):
        self.assertTrue(tetrahedral_number(2147483647) > 0)  # Check that it returns a valid result

