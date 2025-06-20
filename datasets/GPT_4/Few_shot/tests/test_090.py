import unittest
from datasets.GPT_4.Few_shot.programs.program_090 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_char_position("hello"), {'h': [0], 'e': [1], 'l': [2, 3], 'o': [4]}) # Repeated and unique characters)

    def test_case_2(self):
        self.assertEqual(count_char_position("abc"), {'a': [0], 'b': [1], 'c': [2]}) # All unique characters)

    def test_case_3(self):
        self.assertEqual(count_char_position(""), {}) # Empty string)

    def test_case_4(self):
        self.assertEqual(count_char_position("aabb"), {'a': [0, 1], 'b': [2, 3]}) # All repeated characters)

    def test_case_5(self):
        self.assertEqual(count_char_position("a b c"), {'a': [0], ' ': [1, 3], 'b': [2], 'c': [4]}) # String with spaces)

    def test_case_6(self):
        self.assertEqual(count_char_position("!@) #"), {'!': [0], '@': [1], '#': [2]})  # Special characters)

    def test_case_7(self):
        self.assertEqual(count_char_position("aaa"), {'a': [0, 1, 2]}) # All identical characters)

    def test_case_8(self):
        self.assertEqual(count_char_position("abac"), {'a': [0, 2], 'b': [1], 'c': [3]}) # Mixed repetition)

