import unittest
from datasets.mbpp.programs.program_028 import *

class TestVersion(unittest.TestCase):
    def test_word_len_with__Hadoop__expect_False(self):
        self.assertEqual(word_len("Hadoop"), False)

    def test_word_len_with__great__expect_True(self):
        self.assertEqual(word_len("great"), True)

    def test_word_len_with__structure__expect_True(self):
        self.assertEqual(word_len("structure"), True)

