import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_097 import *

class TestVersion(unittest.TestCase):
    def test_all_same_type(self):
        self.assertTrue(check_type((1, 2, 3, 4)))

    def test_mixed_data_types(self):
        self.assertFalse(check_type((1, 'string', 3.0)))

    def test_empty_tuple(self):
        self.assertTrue(check_type(()))

    def test_single_element_tuple(self):
        self.assertTrue(check_type((1,)))

    def test_tuple_with_nested_tuples(self):
        self.assertTrue(check_type(((1, 2), (3, 4))))

    def test_tuple_with_strings(self):
        self.assertTrue(check_type(('a', 'b', 'c')))

    def test_tuple_with_integers(self):
        self.assertTrue(check_type((1, 2, 3)))

    def test_tuple_with_floats(self):
        self.assertTrue(check_type((1.1, 2.2, 3.3)))

    def test_tuple_with_complex_numbers(self):
        self.assertTrue(check_type((1+2j, 3+4j)))

    def test_large_tuple(self):
        large_tuple = (1,) * 10000
        self.assertTrue(check_type(large_tuple))

