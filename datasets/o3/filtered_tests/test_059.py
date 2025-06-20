import unittest
from datasets.o3.programs.program_059 import *

class TestVersion(unittest.TestCase):
    def test_all_empty_dicts(self):
        self.assertTrue(empty_dit([{}, {}]))

    def test_contains_non_empty_dict(self):
        self.assertFalse(empty_dit([{}, {"a":1}]))

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

