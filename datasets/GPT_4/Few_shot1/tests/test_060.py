import unittest
from datasets.GPT_4.Few_shot1.programs.program_060 import *

class TestVersion(unittest.TestCase):
    def test_tuple_to_int_basic(self): self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_tuple_to_int_single_digit(self): self.assertEqual(tuple_to_int((7,)), 7)

    def test_tuple_to_int_leading_zeros(self): self.assertEqual(tuple_to_int((0, 1, 2)), 12)

    def test_tuple_to_int_all_zeros(self): self.assertEqual(tuple_to_int((0, 0, 0)), 0)

    def test_tuple_to_int_large(self): self.assertEqual(tuple_to_int((9, 8, 7, 6, 5)), 98765)

    def test_tuple_to_int_non_integer_elements(self): self.assertEqual(tuple_to_int(('1', 2, '3')), 123)

