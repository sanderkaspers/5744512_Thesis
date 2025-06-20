import unittest
from datasets.GPT_4.Few_shot.programs.program_001 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(remove_Occ("", "a"), "")

    def test_case_2(self):
        self.assertEqual(remove_Occ("banana", "a"), "bnn")

    def test_case_3(self):
        self.assertEqual(remove_Occ("apple", "b"), "apple")

    def test_case_4(self):
        self.assertEqual(remove_Occ("aaaaa", "a"), "")

    def test_case_5(self):
        self.assertEqual(remove_Occ("abracadabra", "a"), "brcdbr")

    def test_case_6(self):
        self.assertEqual(remove_Occ("abcde", "a"), "bcde")

    def test_case_7(self):
        self.assertEqual(remove_Occ("abcde", "e"), "abcd")

    def test_case_8(self):
        self.assertEqual(remove_Occ("Hello, World!", "o"), "Hell, Wrld!")

    def test_case_9(self):
        self.assertEqual(remove_Occ("abcdef", "z"), "abcdef")

    def test_case_10(self):
        self.assertEqual(remove_Occ("xyzxyz", "x"), "yzyz")

