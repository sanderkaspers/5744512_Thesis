import unittest
from datasets.GPT_4.Zero_shot1.programs.program_073 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")

    def test_2(self):
        self.assertEqual(reverse_vowels("rhythm"), "rhythm")

    def test_3(self):
        self.assertEqual(reverse_vowels("apple"), "eppla")

    def test_4(self):
        self.assertEqual(reverse_vowels("ApPlE"), "EpPlA")

    def test_5(self):
        self.assertEqual(reverse_vowels("a"), "a")

    def test_6(self):
        self.assertEqual(reverse_vowels("z"), "z")

    def test_7(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_8(self):
        self.assertEqual(reverse_vowels("a b e"), "e b a")

    def test_9(self):
        self.assertIsInstance(reverse_vowels("test"), str)

