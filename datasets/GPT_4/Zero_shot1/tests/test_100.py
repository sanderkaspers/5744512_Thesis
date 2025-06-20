import unittest
from datasets.GPT_4.Zero_shot1.programs.program_100 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(odd_values_string("abcde"), "ace")

    def test_2(self):
        self.assertEqual(odd_values_string("x"), "x")

    def test_3(self):
        self.assertEqual(odd_values_string(""), "")

    def test_4(self):
        self.assertEqual(odd_values_string("a!b@c#d$"), "a!c$")

    def test_5(self):
        self.assertEqual(odd_values_string("a b c d"), "abc")

    def test_6(self):
        self.assertEqual(odd_values_string("aaaaaa"), "aaa")

    def test_7(self):
        self.assertEqual(odd_values_string("1234567890"), "13579")

    def test_8(self):
        self.assertEqual(odd_values_string("a"*1000), "a"*500)

    def test_9(self):
        self.assertIsInstance(odd_values_string("abc"), str)

    def test_10(self):
        self.assertEqual(odd_values_string("áéíóú"), "áíú")

    def test_11(self):
        self.assertEqual(odd_values_string("a\nb\nc\nd"), "abc")

