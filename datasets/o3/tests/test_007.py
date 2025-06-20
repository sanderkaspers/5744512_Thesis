import unittest
from datasets.o3.programs.program_007 import *

class TestVersion(unittest.TestCase):
    def test_duplicates_present(self):
        self.assertTrue(test_duplicate([1, 2, 3, 2]))

    def test_no_duplicates(self):
        self.assertFalse(test_duplicate([1, 2, 3]))

    def test_empty_list(self):
        self.assertFalse(test_duplicate([]))

    def test_string_duplicates(self):
        self.assertTrue(test_duplicate(["a", "b", "a"]))

    def test_large_list_duplicates(self):
        large_list = list(range(1000)) + [999]
        self.assertTrue(test_duplicate(large_list))

