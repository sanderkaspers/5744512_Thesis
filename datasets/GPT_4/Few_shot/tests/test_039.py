import unittest
from datasets.GPT_4.Few_shot.programs.program_039 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_substring("hello world", "world"), True) # Substring exists)

    def test_case_2(self):
        self.assertEqual(find_substring("hello world", "planet"), False) # Substring does not exist)

    def test_case_3(self):
        self.assertEqual(find_substring("apple", "app"), True) # Substring at start)

    def test_case_4(self):
        self.assertEqual(find_substring("apple", "le"), True) # Substring at end)

    def test_case_5(self):
        self.assertEqual(find_substring("apple pie", "pie"), True) # Substring as a separate word)

    def test_case_6(self):
        self.assertEqual(find_substring("", "test"), False) # Empty string)

    def test_case_7(self):
        self.assertEqual(find_substring("test", ""), True) # Empty substring)

    def test_case_8(self):
        self.assertEqual(find_substring("special$chars", "$chars"), True) # Substring with special characters)

