import unittest
from datasets.o3.programs.program_077 import *

class TestVersion(unittest.TestCase):
    def test_mixed_list_returns_ratio(self):
        self.assertAlmostEqual(zero_count([0, 1, 0, 2]), 1.0)

    def test_no_zeros_returns_zero(self):
        self.assertEqual(zero_count([1, 2, 3]), 0)

    def test_all_zeros_raises(self):
        with self.assertRaises(ZeroDivisionError):
            zero_count([0, 0, 0])

    def test_float_values(self):
        self.assertAlmostEqual(zero_count([0.0, 0, 1.5, -2]), 2/2)

    def test_array_input(self):
        from array import array
        nums = array('i', [0, 0, 3, 4])
        self.assertAlmostEqual(zero_count(nums), 2/2)

    def test_negative_and_zero(self):
        self.assertAlmostEqual(zero_count([0, -1, -2, 0]), 2/2)

