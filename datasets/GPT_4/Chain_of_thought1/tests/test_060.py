import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_060 import *

class TestVersion(unittest.TestCase):
    def test_normal_digits(self): self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_single_digit(self): self.assertEqual(tuple_to_int((5,)), 5)

    def test_leading_zero(self): self.assertEqual(tuple_to_int((0, 1, 2)), 12)

    def test_all_zeros(self): self.assertEqual(tuple_to_int((0, 0, 0)), 0)

    def test_string_digits(self): self.assertEqual(tuple_to_int(('1', '2', '3')), 123)

    def test_mixed_str_int(self): self.assertEqual(tuple_to_int((1, '2', 3)), 123)

    def test_list_input(self): self.assertEqual(tuple_to_int([4, 5, 6]), 456)

    def test_negative_digit(self): self.assertEqual(tuple_to_int((-1, 2, 3)), -123)

