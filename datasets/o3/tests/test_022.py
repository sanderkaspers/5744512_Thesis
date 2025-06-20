import unittest
from datasets.o3.programs.program_022 import *

class TestVersion(unittest.TestCase):
    def test_all_equal_length(self):
        self.assertTrue(get_equal([(1,2), (3,4), (5,6)]))

    def test_not_equal_length(self):
        self.assertFalse(get_equal([(1,), (2,3)]))

    def test_empty_input(self):
        self.assertTrue(get_equal([]))

    def test_single_tuple(self):
        self.assertTrue(get_equal([(1,2,3)]))

    def test_empty_tuples(self):
        self.assertTrue(get_equal([(), ()]))

    def test_first_tuple_longer(self):
        self.assertFalse(get_equal([(1,2,3), (4,5)]))

