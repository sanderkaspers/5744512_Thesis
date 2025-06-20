import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_097 import *

class TestVersion(unittest.TestCase):
    def test_all_integers(self): self.assertTrue(check_type((1, 2, 3, 4)))

    def test_all_strings(self): self.assertTrue(check_type(('a', 'b', 'c')))

    def test_all_floats(self): self.assertTrue(check_type((1.1, 2.2, 3.3)))

    def test_all_booleans(self): self.assertTrue(check_type((True, False, True)))

    def test_mixed_int_and_float(self): self.assertFalse(check_type((1, 2.0, 3)))

    def test_first_differs_from_rest(self): self.assertFalse(check_type(('1', 1, 1)))

    def test_empty_tuple(self): self.assertTrue(check_type(()))

    def test_single_element_tuple(self): self.assertTrue(check_type((42,)))

    def test_nested_same_type(self): self.assertTrue(check_type(([1], [2], [3])))

    def test_mixed_nested_types(self): self.assertFalse(check_type(([1], {'a': 1})))

