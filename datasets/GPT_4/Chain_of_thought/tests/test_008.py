import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_008 import *

class TestVersion(unittest.TestCase):
    def test_typical_odd_not_woodall(self):
        self.assertFalse(is_woodall(7))

    def test_typical_odd_woodall(self):
        self.assertTrue(is_woodall(3))

    def test_even_number(self):
        self.assertFalse(is_woodall(8))

    def test_one_as_input(self):
        self.assertTrue(is_woodall(1))

    def test_negative_number(self):
        self.assertFalse(is_woodall(-5))

    def test_zero_as_input(self):
        self.assertFalse(is_woodall(0))

    def test_large_odd_number(self):
        self.assertFalse(is_woodall(999999))

    def test_prime_number(self):
        self.assertFalse(is_woodall(13))

    def test_just_below_woodall(self):
        self.assertFalse(is_woodall(2))

    def test_just_above_woodall(self):
        self.assertFalse(is_woodall(5))

    def test_floating_point_number(self):
        with self.assertRaises(TypeError):
            is_woodall(4.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            is_woodall('7')

    def test_multiple_of_two_plus_one(self):
        self.assertTrue(is_woodall(1))

    def test_known_woodall_number(self):
        self.assertTrue(is_woodall(15))

    def test_fractional_number(self):
        with self.assertRaises(TypeError):
            is_woodall(5.75)

