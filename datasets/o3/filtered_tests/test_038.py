import unittest
from datasets.o3.programs.program_038 import *

class TestVersion(unittest.TestCase):
    def test_mixed_lengths(self):
        self.assertEqual(len_log(["a","ab","abc"]), 3)

    def test_equal_lengths(self):
        self.assertEqual(len_log(["aa","bb","cc"]), 2)

    def test_contains_empty_string(self):
        self.assertEqual(len_log(["", "a", "abcde"]), 5)

    def test_single_element(self):
        self.assertEqual(len_log(["hello"]), 5)

    def test_unicode_characters(self):
        self.assertEqual(len_log(["π","αβ","γδεζη"]), 5)

    def test_whitespace_string(self):
        self.assertEqual(len_log([" " * 10, "x"]), 10)

    def test_empty_list_raises(self):
        with self.assertRaises(IndexError):
            len_log([])

