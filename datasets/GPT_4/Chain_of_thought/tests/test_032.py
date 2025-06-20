import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_032 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sequence(5), 3)

    def test_base_case_n_1(self):
        self.assertEqual(sequence(1), 1)

    def test_base_case_n_2(self):
        self.assertEqual(sequence(2), 1)

    def test_larger_n(self):
        self.assertEqual(sequence(10), 6)

    def test_negative_n(self):
        with self.assertRaises(RecursionError):
            sequence(-5)

    def test_zero_n(self):
        with self.assertRaises(RecursionError):
            sequence(0)

    def test_floating_point_n(self):
        with self.assertRaises(TypeError):
            sequence(5.5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sequence('10')

    def test_performance_large_n(self):
        self.assertTrue(sequence(20) > 0)

