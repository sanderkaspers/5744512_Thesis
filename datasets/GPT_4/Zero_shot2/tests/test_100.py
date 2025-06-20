import unittest
from datasets.GPT_4.Zero_shot2.programs.program_100 import *

class TestVersion(unittest.TestCase):
    def test_odd_1(self):
        self.assertEqual(odd_values_string("abcdef"), "bdf")

    def test_odd_2(self):
        self.assertEqual(odd_values_string(""), "")

    def test_odd_3(self):
        self.assertEqual(odd_values_string("a"), "")

    def test_odd_4(self):
        self.assertEqual(odd_values_string("abcd"), "bd")

    def test_odd_5(self):
        self.assertEqual(odd_values_string("abcde"), "bd")

    def test_odd_6(self):
        self.assertEqual(odd_values_string("@#%&*"), "#&")

    def test_odd_7(self):
        self.assertEqual(odd_values_string("a b c d"), "   ")

    def test_odd_8(self):
        self.assertEqual(odd_values_string("AbCdEf"), "bdf")

    def test_odd_9(self):
        self.assertEqual(odd_values_string("1234567"), "246")

    def test_odd_10(self):
        self.assertEqual(odd_values_string("a"*1000), "a"*500)

