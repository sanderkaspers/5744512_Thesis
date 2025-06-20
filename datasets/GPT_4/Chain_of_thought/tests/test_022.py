import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_022 import *

class TestVersion(unittest.TestCase):
    def test_tuples_same_length(self):
        self.assertTrue(get_equal([(1, 2), (3, 4), (5, 6)]))

    def test_tuples_different_lengths(self):
        self.assertFalse(get_equal([(1, 2), (3, 4, 5), (6,)]))

    def test_single_tuple(self):
        self.assertTrue(get_equal([(1, 2, 3)]))

    def test_empty_list(self):
        self.assertTrue(get_equal([]))

    def test_empty_tuples(self):
        self.assertTrue(get_equal([(), (), ()]))

    def test_mixed_empty_non_empty_tuples(self):
        self.assertFalse(get_equal([(), (1,), (2, 3)]))

    def test_large_tuples(self):
        self.assertTrue(get_equal([(1,) * 1000, (2,) * 1000]))

    def test_mixed_data_types(self):
        self.assertTrue(get_equal([(1, 'a'), (2, 'b'), (3, 'c')]))

    def test_floating_point_numbers(self):
        self.assertTrue(get_equal([(1.1, 2.2), (3.3, 4.4), (5.5, 6.6)]))

    def test_boundary_max_tuple_size(self):
        self.assertTrue(get_equal([(1,) * 10000, (2,) * 10000]))

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            get_equal('not a list of tuples')

    def test_nested_tuples(self):
        self.assertTrue(get_equal([((1, 2),), ((3, 4),)]))

