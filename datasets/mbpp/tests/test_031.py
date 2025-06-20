import unittest
from datasets.mbpp.programs.program_031 import *

class TestVersion(unittest.TestCase):
    def test_get_Char_with_abc_expect_f(self):
        self.assertEqual(get_Char("abc"), "f")

    def test_get_Char_with_gfg_expect_t(self):
        self.assertEqual(get_Char("gfg"), "t")

    def test_get_Char_with_ab_expect_c(self):
        self.assertEqual(get_Char("ab"), "c")

