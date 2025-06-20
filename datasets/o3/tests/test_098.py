import unittest
from datasets.o3.programs.program_098 import *

class TestVersion(unittest.TestCase):
    def test_majority_exists(self):
        arr = [2, 2, 2, 3, 3]
        self.assertTrue(is_majority(arr, len(arr), 2))

    def test_no_majority(self):
        arr = [2, 2, 3, 3, 3]
        self.assertFalse(is_majority(arr, len(arr), 2))

    def test_exact_half(self):
        arr = [1, 1, 2, 2]
        self.assertFalse(is_majority(arr, len(arr), 1))

    def test_element_absent(self):
        arr = [1, 2, 3, 4]
        self.assertFalse(is_majority(arr, len(arr), 5))

