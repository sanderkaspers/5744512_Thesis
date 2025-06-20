import unittest
from datasets.o3.programs.program_027 import *

class TestVersion(unittest.TestCase):
    def test_positive_multiple_of_11(self):
        self.assertTrue(is_Diff(22))

    def test_positive_not_multiple_of_11(self):
        self.assertFalse(is_Diff(23))

    def test_zero(self):
        self.assertTrue(is_Diff(0))

    def test_negative_multiple_of_11(self):
        self.assertTrue(is_Diff(-33))

    def test_negative_not_multiple_of_11(self):
        self.assertFalse(is_Diff(-32))

