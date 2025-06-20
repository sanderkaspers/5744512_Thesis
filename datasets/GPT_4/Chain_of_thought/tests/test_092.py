import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_092 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(next_power_of_2(10), 16)

    def test_power_of_2(self):
        self.assertEqual(next_power_of_2(16), 16)

    def test_smallest_power_of_2(self):
        self.assertEqual(next_power_of_2(1), 1)

    def test_zero_input(self):
        self.assertEqual(next_power_of_2(0), 1)

    def test_negative_input(self):
        self.fail("Negative input not supported by implementation; test would hang.") #    with self.assertRaises(ValueError):
        #        next_power_of_2(-5)

    def test_large_input(self):
        self.assertEqual(next_power_of_2(123456789), 134217728)

    def test_one_less_than_power_of_2(self):
        self.assertEqual(next_power_of_2(15), 16)

    def test_one_more_than_power_of_2(self):
        self.assertEqual(next_power_of_2(17), 32)

    def test_floating_point_input(self):
        with self.assertRaises(TypeError):
            next_power_of_2(15.5)

    def test_max_integer(self):
        self.assertEqual(next_power_of_2(2**31 - 1), 2**31)

