import unittest
from datasets.mbpp.programs.program_090 import *

class TestVersion(unittest.TestCase):
    def test_count_char_position_with__xbcefg__expect_2(self):
        self.assertEqual(count_char_position("xbcefg"), 2)

    def test_count_char_position_with__ABcED__expect_3(self):
        self.assertEqual(count_char_position("ABcED"), 3)

    def test_count_char_position_with__AbgdeF__expect_5(self):
        self.assertEqual(count_char_position("AbgdeF"), 5)

