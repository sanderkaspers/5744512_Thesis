import unittest
from datasets.o3.programs.program_058 import *

class TestVersion(unittest.TestCase):
    def test_positive_int(self):
        self.assertTrue(check_integer("123"))

    def test_plus_sign(self):
        self.assertTrue(check_integer("+456"))

    def test_minus_sign(self):
        self.assertTrue(check_integer("-42"))

    def test_whitespace(self):
        self.assertTrue(check_integer(" 999 "))

    def test_invalid_characters(self):
        self.assertFalse(check_integer("12a"))

    def test_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_single_plus(self):
        self.assertTrue(check_integer("+"))

