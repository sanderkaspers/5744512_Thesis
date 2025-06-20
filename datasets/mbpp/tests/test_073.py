import unittest
from datasets.mbpp.programs.program_073 import *

class TestVersion(unittest.TestCase):
    def test_reverse_vowels_with__Python__expect__Python_(self):
        self.assertEqual(reverse_vowels("Python"), "Python")

    def test_reverse_vowels_with__USA__expect__ASU_(self):
        self.assertEqual(reverse_vowels("USA"), "ASU")

    def test_reverse_vowels_with__ab__expect__ab_(self):
        self.assertEqual(reverse_vowels("ab"), "ab")

