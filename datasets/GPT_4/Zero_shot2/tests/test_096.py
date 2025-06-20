import unittest
from datasets.GPT_4.Zero_shot2.programs.program_096 import *

class TestVersion(unittest.TestCase):
    def test_occ_1(self):
        self.assertEqual(count_occurance("aeiou"), 5)

    def test_occ_2(self):
        self.assertEqual(count_occurance("AEIOU"), 5)

    def test_occ_3(self):
        self.assertEqual(count_occurance("Hello World"), 3)

    def test_occ_4(self):
        self.assertEqual(count_occurance("rhythm"), 0)

    def test_occ_5(self):
        self.assertEqual(count_occurance(""), 0)

    def test_occ_6(self):
        self.assertEqual(count_occurance("aAaAaA"), 6)

    def test_occ_7(self):
        self.assertEqual(count_occurance("123!@#"), 0)

    def test_occ_8(self):
        self.assertEqual(count_occurance("oOoO"), 4)

    def test_occ_9(self):
        self.assertEqual(count_occurance("a" * 1000), 1000)

    def test_occ_10(self):
        self.assertEqual(count_occurance("     "), 0)

