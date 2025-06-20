import unittest
from datasets.o3.programs.program_073 import *

class TestVersion(unittest.TestCase):
    def test_reverse_vowels_basic(self):
        self.assertEqual(reverse_vowels("hello"), "holle")

    def test_no_vowels_returns_same(self):
        self.assertEqual(reverse_vowels("rhythm"), "rhythm")

    def test_all_vowels_reversed(self):
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")

    def test_empty_string(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_uppercase_handling(self):
        self.assertEqual(reverse_vowels("HELLO"), "HOLLE")

