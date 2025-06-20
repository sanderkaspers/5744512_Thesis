import unittest
from datasets.GPT_4.Few_shot.programs.program_013 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_frequencies(""), {}) # Empty string)

    def test_case_2(self):
        self.assertEqual(count_frequencies("a"), {'a': 1}) # Single character)

    def test_case_3(self):
        self.assertEqual(count_frequencies("abca"), {'a': 2, 'b': 1, 'c': 1}) # Repeated characters)

    def test_case_4(self):
        self.assertEqual(count_frequencies("abcd"), {'a': 1, 'b': 1, 'c': 1, 'd': 1}) # Unique characters)

    def test_case_5(self):
        self.assertEqual(count_frequencies("a! b@ c) #"), {'a': 1, '!': 1, ' ': 2, 'b': 1, '@': 1, 'c': 1, '#': 1})  # Special characters and spaces

    def test_case_6(self):
        self.assertEqual(count_frequencies("1111"), {'1': 4}) # All identical characters)

    def test_case_7(self):
        self.assertEqual(count_frequencies("Aaaa"), {'A': 1, 'a': 3}) # Case sensitivity)

    def test_case_8(self):
        self.assertEqual(count_frequencies(" "), {' ': 1}) # Single space)

