import unittest
from datasets.o3.programs.program_060 import *

class TestVersion(unittest.TestCase):
    def test_basic_tuple(self):
        self.assertEqual(tuple_to_int((1,2,3)), 123)

    def test_leading_zeroes(self):
        self.assertEqual(tuple_to_int((0,0,5)), 5)

    def test_single_digit(self):
        self.assertEqual(tuple_to_int((7,)), 7)

    def test_negative_number_in_tuple(self):
        with self.assertRaises(ValueError):
            tuple_to_int((1,-2))

    def test_empty_tuple(self):
        with self.assertRaises(ValueError):
            tuple_to_int(())

