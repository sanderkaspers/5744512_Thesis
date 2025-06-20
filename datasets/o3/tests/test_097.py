import unittest
from datasets.o3.programs.program_097 import *

class TestVersion(unittest.TestCase):
    def test_all_ints(self):
        self.assertTrue(check_type((1, 2, 3, 4)))

    def test_all_floats(self):
        self.assertTrue(check_type((1.0, 2.5, 3.14)))

    def test_mixed_types(self):
        self.assertFalse(check_type((1, "a", 3)))

    def test_single_element(self):
        self.assertTrue(check_type((True,)))

    def test_empty_tuple(self):
        self.assertTrue(check_type(()))

