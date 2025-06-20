import unittest
from datasets.o3.programs.program_074 import *

class TestVersion(unittest.TestCase):
    def test_basic_char_tuple(self):
        tup1 = ('p','y','t','h','o','n')
        self.assertEqual(tup_string(tup1), "python")

    def test_empty_tuple_returns_empty_string(self):
        self.assertEqual(tup_string(tuple()), "")

    def test_tuple_integers_raises(self):
        with self.assertRaises(TypeError):
            tup_string((1,2,3))

    def test_tuple_with_spaces(self):
        tup1 = ('hello',' ','world')
        self.assertEqual(tup_string(tup1), "hello world")

    def test_tuple_with_unicode_characters(self):
        tup1 = ('π','ρ','ο','γ','ρ','α','μ')
        self.assertEqual(tup_string(tup1), "προγραμ")

