import unittest
from datasets.o3.programs.program_031 import *

class TestVersion(unittest.TestCase):
    def test_get_char_simple_sum(self):
        self.assertEqual(get_Char("abc"), 'f')

    def test_get_char_wraps_to_z(self):
        self.assertEqual(get_Char("z"), 122)

    def test_get_char_multiple_wrap(self):
        self.assertEqual(get_Char("zzz"), 122)

    def test_get_char_empty_string(self):
        self.assertEqual(get_Char(""), 122)

    def test_get_char_long_string(self):
        self.assertEqual(get_Char("abcdefghijklmnopqrstuvwxyz"), 'm')

