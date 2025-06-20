import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_087 import *

class TestVersion(unittest.TestCase):
    def test_typical_case_odd(self):
        self.assertEqual(sum_series(7), 16)

    def test_even_n(self):
        self.assertEqual(sum_series(8), 20)

    def test_small_n_1(self):
        self.assertEqual(sum_series(1), 1)

    def test_small_n_2(self):
        self.assertEqual(sum_series(2), 2)

    def test_n_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_negative_n(self):
        self.assertEqual(sum_series(-5), 0)

    def test_large_n(self):
        self.assertEqual(sum_series(1000), 250500)

    def test_floating_point_n(self):
        with self.assertRaises(TypeError):
            sum_series(7.5)

    def test_non_integer_n(self):
        with self.assertRaises(TypeError):
            sum_series('10')

    def test_n_equals_3(self):
        self.assertEqual(sum_series(3), 4)

