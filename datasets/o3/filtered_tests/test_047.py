import unittest
from datasets.o3.programs.program_047 import *

class TestVersion(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "0")

    def test_small_positive(self):
        self.assertEqual(decimal_to_binary(5), "101")

    def test_large_positive(self):
        self.assertEqual(decimal_to_binary(1023), "1111111111")

    def test_negative(self):
        self.assertEqual(decimal_to_binary(-5), "-101")

    def test_no_prefix(self):
        self.assertFalse(decimal_to_binary(8).startswith("0b"))

    def test_non_integer_raises(self):
        with self.assertRaises(TypeError):
            decimal_to_binary(5.5)

