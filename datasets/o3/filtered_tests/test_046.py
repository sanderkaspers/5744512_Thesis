import unittest
from datasets.o3.programs.program_046 import *

class TestVersion(unittest.TestCase):
    def test_average_positive_ints(self):
        self.assertEqual(multiply_num([1, 2, 3, 4]), 6.0)

    def test_single_element(self):
        self.assertEqual(multiply_num([5]), 5.0)

    def test_contains_zero(self):
        self.assertEqual(multiply_num([0, 1, 2]), 0.0)

    def test_negative_numbers(self):
        self.assertEqual(multiply_num([-1, 2, -3]), 2.0)

    def test_floats(self):
        self.assertAlmostEqual(multiply_num([1.5, 2.5]), 1.875, places=3)

    def test_empty_list_raises(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([])

