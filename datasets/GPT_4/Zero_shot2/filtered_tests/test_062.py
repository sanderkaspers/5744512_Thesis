import unittest
from datasets.GPT_4.Zero_shot2.programs.program_062 import *

class TestVersion(unittest.TestCase):
    def test_str_1(self):
        self.assertEqual(string_to_list("this is a test"), ["this", "is", "a", "test"])

    def test_str_2(self):
        self.assertEqual(string_to_list("split  this  string"), ["split", "", "this", "", "string"])

    def test_str_3(self):
        self.assertEqual(string_to_list(""), [""])

    def test_str_4(self):
        self.assertEqual(string_to_list("hello"), ["hello"])

    def test_str_5(self):
        self.assertEqual(string_to_list("  hello world  "), ["", "", "hello", "world", "", ""])

    def test_str_6(self):
        self.assertEqual(string_to_list("   "), ["", "", "", ""])

    def test_str_7(self):
        self.assertEqual(string_to_list("line1\nline2\tline3"), ["line1\nline2\tline3"])

