import unittest
from datasets.GPT_4.Few_shot.programs.program_073 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(reverse_vowels("hello"), "holle") # Simple case)

    def test_case_2(self):
        self.assertEqual(reverse_vowels("leetcode"), "leotcede") # Multiple vowels)

    def test_case_3(self):
        self.assertEqual(reverse_vowels("aeiou"), "uoiea") # All vowels)

    def test_case_4(self):
        self.assertEqual(reverse_vowels("bcdfg"), "bcdfg") # No vowels)

    def test_case_5(self):
        self.assertEqual(reverse_vowels("AEIOU"), "UOIEA") # All uppercase vowels)

    def test_case_6(self):
        self.assertEqual(reverse_vowels(""), "") # Empty string)

    def test_case_7(self):
        self.assertEqual(reverse_vowels("aA"), "Aa") # Mixed case vowels)

    def test_case_8(self):
        self.assertEqual(reverse_vowels("united"), "enitud") # Mixed consonants and vowels)

