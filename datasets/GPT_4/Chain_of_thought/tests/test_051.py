import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_051 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(eulerian_num(4, 2), 11)

    def test_m_equals_zero(self):
        self.assertEqual(eulerian_num(5, 0), 1)

    def test_m_equals_n_minus_one(self):
        self.assertEqual(eulerian_num(5, 4), 16)

    def test_m_greater_or_equal_to_n(self):
        self.assertEqual(eulerian_num(4, 4), 0)
        self.assertEqual(eulerian_num(4, 5), 0)

    def test_n_equals_zero(self):
        self.assertEqual(eulerian_num(0, 0), 0)
        self.assertEqual(eulerian_num(0, 1), 0)

    def test_negative_inputs(self):
        self.assertEqual(eulerian_num(-4, 2), 0)
        self.assertEqual(eulerian_num(4, -2), 0)

    def test_large_inputs(self):
        self.assertEqual(eulerian_num(10, 5), 42525)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            eulerian_num(4.5, 2)
        with self.assertRaises(TypeError):
            eulerian_num('4', 2)

