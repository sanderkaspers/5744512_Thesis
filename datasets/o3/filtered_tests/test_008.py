import unittest
from datasets.o3.programs.program_008 import *

class TestVersion(unittest.TestCase):
    def test_woodall_one(self):
        self.assertTrue(is_woodall(1))

    def test_woodall_seven(self):
        self.assertTrue(is_woodall(7))

    def test_woodall_twenty_three(self):
        self.assertTrue(is_woodall(23))

    def test_even_number(self):
        self.assertFalse(is_woodall(4))

    def test_non_woodall_odd(self):
        self.assertFalse(is_woodall(5))

    def test_large_non_woodall(self):
        self.assertFalse(is_woodall(13))

