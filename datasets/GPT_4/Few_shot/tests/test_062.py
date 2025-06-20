import unittest
from datasets.GPT_4.Few_shot.programs.program_062 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(string_to_list("abc"), ['a', 'b', 'c']) # Simple string)

    def test_case_2(self):
        self.assertEqual(string_to_list(""), []) # Empty string)

    def test_case_3(self):
        self.assertEqual(string_to_list("a b c"), ['a', ' ', 'b', ' ', 'c']) # String with spaces)

    def test_case_4(self):
        self.assertEqual(string_to_list("123"), ['1', '2', '3']) # Numeric string)

    def test_case_5(self):
        self.assertEqual(string_to_list("!@) #"), ['!', '@', '#'] ) # String with special characters)

    def test_case_6(self):
        self.assertEqual(string_to_list("a"), ['a']) # Single character)

    def test_case_7(self):
        self.assertEqual(string_to_list("abc\n"), ['a', 'b', 'c', '\n']) # String with newline)

    def test_case_8(self):
        self.assertEqual(string_to_list("hello world!"), ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']) # String with punctuation and space)

