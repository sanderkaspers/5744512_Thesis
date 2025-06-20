import unittest
from datasets.o3.programs.program_024 import *

class TestVersion(unittest.TestCase):
    def test_multiple_of_four(self):
        self.assertTrue(dif_Square(8))

    def test_mod_one(self):
        self.assertTrue(dif_Square(5))

    def test_mod_two(self):
        self.assertFalse(dif_Square(6))

    def test_mod_three(self):
        self.assertTrue(dif_Square(7))

    def test_negative_mod_two(self):
        self.assertFalse(dif_Square(-2))

