import unittest
from datasets.GPT_4.Zero_shot2.programs.program_073 import *

class TestVersion(unittest.TestCase):
    def test_vow_1(self):
        self.assertEqual(reverse_vowels("hello"), "holle")

    def test_vow_2(self):
        self.assertEqual(reverse_vowels("bcdfg"), "bcdfg")

    def test_vow_3(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_vow_4(self):
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")

    def test_vow_5(self):
        self.assertEqual(reverse_vowels("AEIOU"), "UOIEA")

    def test_vow_6(self):
        self.assertEqual(reverse_vowels("aEiOu"), "uOiEa")

    def test_vow_7(self):
        self.assertEqual(reverse_vowels("h@llO wOrld!"), "h@llO wOrld!")

    def test_vow_8(self):
        self.assertEqual(reverse_vowels("aabbcc"), "aabbcc")

    def test_vow_9(self):
        self.assertEqual(reverse_vowels("a"), "a")

    def test_vow_10(self):
        self.assertEqual(reverse_vowels("b"), "b")

