import unittest
from datasets.o3.programs.program_100 import *

class TestVersion(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(odd_values_string(""), "")

    def test_even_length(self):
        self.assertEqual(odd_values_string("abcdef"), "ace")

    def test_odd_length(self):
        self.assertEqual(odd_values_string("abcde"), "ace")

    def test_single_char(self):
        self.assertEqual(odd_values_string("x"), "x")

    def test_unicode(self):
        self.assertEqual(odd_values_string("áéíóú"), "áíú")

