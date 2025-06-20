import unittest
from datasets.GPT_4.Few_shot.programs.program_028 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(word_len("Hello world"), [5, 5]) # Two words)

    def test_case_2(self):
        self.assertEqual(word_len("Hi"), [2]) # Single word)

    def test_case_3(self):
        self.assertEqual(word_len(""), [0]) # Empty string)

    def test_case_4(self):
        self.assertEqual(word_len("This is a test"), [4, 2, 1, 4]) # Multiple words)

    def test_case_5(self):
        self.assertEqual(word_len("A B C"), [1, 1, 1]) # Single-letter words)

    def test_case_6(self):
        self.assertEqual(word_len("Hello, world!"), [6, 6]) # Words with punctuation)

    def test_case_7(self):
        self.assertEqual(word_len("word\nnewline"), [4, 7])  # Word with newline character

    def test_case_8(self):
        self.assertEqual(word_len("   "), [0, 0, 0]) # String with only spaces)

