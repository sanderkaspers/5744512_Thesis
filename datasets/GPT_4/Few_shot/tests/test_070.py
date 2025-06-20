import unittest
from datasets.GPT_4.Few_shot.programs.program_070 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(long_words(3, "this is a test"), ["this", "test"]) # Words longer than 3)

    def test_case_2(self):
        self.assertEqual(long_words(4, "hello world"), ["hello", "world"]) # All words longer than 4)

    def test_case_3(self):
        self.assertEqual(long_words(4, "a bb ccc dddd"), ["dddd"]) # Only one word longer than 4)

    def test_case_4(self):
        self.assertEqual(long_words(0, "one two three"), ["one", "two", "three"]) # All words longer than 0)

    def test_case_5(self):
        self.assertEqual(long_words(5, "short and longword"), ["longword"]) # Mixed word lengths)

    def test_case_6(self):
        self.assertEqual(long_words(10, "no long words here"), []) # No words longer than 10)

    def test_case_7(self):
        self.assertEqual(long_words(3, ""), []) # Empty string)

    def test_case_8(self):
        self.assertEqual(long_words(2, "one two three four"), ["one", "two", "three", "four"]) # All words longer than 2)

