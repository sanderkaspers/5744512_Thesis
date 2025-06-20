import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_060 import *

class TestVersion(unittest.TestCase):
    def test_single_digit_tuple(self): self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_multi_digit_elements(self): self.assertEqual(tuple_to_int((12, 34, 56)), 123456)

    def test_single_element_tuple(self): self.assertEqual(tuple_to_int((7,)), 7)

    def test_tuple_with_zeroes(self): self.assertEqual(tuple_to_int((0, 1, 0)), 10)

    def test_tuple_starting_with_zero(self): self.assertEqual(tuple_to_int((0, 2, 3)), 23)

    def test_tuple_all_zeros(self): self.assertEqual(tuple_to_int((0, 0, 0)), 0)

