import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_060 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_single_integer(self):
        self.assertEqual(tuple_to_int((7,)), 7)

    def test_empty_tuple(self):
        with self.assertRaises(ValueError):
            tuple_to_int(())

    def test_leading_zeros(self):
        self.assertEqual(tuple_to_int((0, 1, 2)), 12)

    def test_large_integers(self):
        self.assertEqual(tuple_to_int((123, 456, 789)), 123456789)

    def test_single_digits(self):
        self.assertEqual(tuple_to_int((4, 5, 6)), 456)

    def test_duplicate_integers(self):
        self.assertEqual(tuple_to_int((11, 11, 11)), 111111)

    def test_non_integer_elements(self):
        with self.assertRaises(ValueError):
            tuple_to_int((1, '2', 3.5))

    def test_mixed_number_of_digits(self):
        self.assertEqual(tuple_to_int((1, 234, 56)), 123456)

    def test_negative_integers(self):
        with self.assertRaises(ValueError):
            tuple_to_int((-1, 2, 3))

