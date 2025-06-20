import unittest
from datasets.GPT_4.Few_shot2.programs.program_043 import *

class TestVersion(unittest.TestCase):
    def test_Find_Min_Length_basic(self): self.assertEqual(Find_Min_Length(['a', 'bb', 'ccc']), ['a'])

    def test_Find_Min_Length_multiple_min(self): self.assertEqual(Find_Min_Length(['hi', 'to', 'on', 'the']), ['hi', 'to', 'on'])

    def test_Find_Min_Length_all_same_length(self): self.assertEqual(Find_Min_Length(['aa', 'bb', 'cc']), ['aa', 'bb', 'cc'])

    def test_Find_Min_Length_single_element(self): self.assertEqual(Find_Min_Length(['single']), ['single'])

    def test_Find_Min_Length_empty_string(self): self.assertEqual(Find_Min_Length(['', 'a', 'ab']), [''])

    def test_Find_Min_Length_all_empty_strings(self): self.assertEqual(Find_Min_Length(['', '', '']), ['', '', ''])

    def test_Find_Min_Length_mixed_lengths(self): self.assertEqual(Find_Min_Length(['apple', 'pie', 'a', 'b', 'banana']), ['a', 'b'])

    def test_Find_Min_Length_numerical_strings(self): self.assertEqual(Find_Min_Length(['1234', '12', '123', '1']), ['1'])

    def test_Find_Min_Length_special_chars(self): self.assertEqual(Find_Min_Length(['!@#', '$', '%^']), ['$'])

    def test_Find_Min_Length_unicode(self): self.assertEqual(Find_Min_Length(['你好', '😊', '👍🏽']), ['😊'])

