import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_097 import *

class TestVersion(unittest.TestCase):
    def test_all_integers(self): self.assertTrue(check_type((1, 2, 3)))

    def test_all_strings(self): self.assertTrue(check_type(('a', 'b', 'c')))

    def test_all_floats(self): self.assertTrue(check_type((1.1, 2.2, 3.3)))

    def test_all_booleans(self): self.assertTrue(check_type((True, False, True)))

    def test_int_and_float(self): self.assertFalse(check_type((1, 2.0)))

    def test_mixed_types(self): self.assertFalse(check_type(('a', 1, 2.0)))

    def test_empty_tuple(self): self.assertTrue(check_type(()))

    def test_singleton_tuple(self): self.assertTrue(check_type((5,)))

    def test_tuple_of_tuples(self): self.assertTrue(check_type(((1,), (2,), (3,))))

    def test_tuple_of_lists(self): self.assertTrue(check_type(([1], [2], [3])))

    def test_all_none(self): self.assertTrue(check_type((None, None)))

    def test_none_and_int(self): self.assertFalse(check_type((None, 5)))

    def test_bool_and_int(self): self.assertFalse(check_type((True, 1)))

    def test_non_tuple_input(self): self.assertTrue(check_type([1, 2, 3]))

