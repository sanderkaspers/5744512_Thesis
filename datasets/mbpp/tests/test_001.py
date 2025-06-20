import unittest
from datasets.mbpp.programs.program_001 import *

class TestVersion(unittest.TestCase):
    def test_remove_Occ_with_hello_l_expect_heo(self):
        self.assertEqual(remove_Occ("hello","l"), "heo")

    def test_remove_Occ_with_abcda_a_expect_bcd(self):
        self.assertEqual(remove_Occ("abcda","a"), "bcd")

    def test_remove_Occ_with_PHP_P_expect_H(self):
        self.assertEqual(remove_Occ("PHP","P"), "H")

