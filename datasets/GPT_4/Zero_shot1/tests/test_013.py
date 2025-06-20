import unittest
from datasets.GPT_4.Zero_shot1.programs.program_013 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_characters("a"), {"a": 1})

    def test_2(self):
        self.assertEqual(count_characters("aaa"), {"a": 3})

    def test_3(self):
        self.assertEqual(count_characters("aA"), {"a": 1, "A": 1})

    def test_4(self):
        self.assertEqual(count_characters("abc123"), {"a": 1, "b": 1, "c": 1, "1": 1, "2": 1, "3": 1})

    def test_5(self):
        self.assertEqual(count_characters("!!??"), {"!": 2, "?": 2})

    def test_6(self):
        self.assertEqual(count_characters(" "), {" ": 1})

    def test_7(self):
        self.assertEqual(count_characters("ññçç"), {"ñ": 2, "ç": 2})

