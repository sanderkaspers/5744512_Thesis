import unittest
from datasets.o3.programs.program_090 import *

class TestVersion(unittest.TestCase):
    def test_general_string(self):
        self.assertEqual(count_char_position("hello"), {'h':[0],'e':[1],'l':[2,3],'o':[4]})

    def test_empty_string(self):
        self.assertEqual(count_char_position(""), {})

    def test_all_same_char(self):
        self.assertEqual(count_char_position("aaaa"), {'a':[0,1,2,3]})

    def test_spaces_and_punctuation(self):
        self.assertEqual(count_char_position("a b,a"), {'a':[0,2],' ':[1],'b':[3],',':[4]})

    def test_unicode_characters(self):
        res = count_char_position("😀🐍😀")
        self.assertEqual(res['😀'], [0,2])
        self.assertEqual(res['🐍'], [1])

    def test_case_sensitivity(self):
        self.assertEqual(count_char_position("AaA"), {'A':[0,2],'a':[1]})

