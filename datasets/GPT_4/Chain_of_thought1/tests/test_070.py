import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_070 import *

class TestVersion(unittest.TestCase):
    def test_mixed_words(self): self.assertEqual(long_words(3, 'This is a test sentence'), ['This', 'test', 'sentence'])

    def test_exact_length_words(self): self.assertEqual(long_words(4, 'word long test'), [])

    def test_all_short(self): self.assertEqual(long_words(5, 'hi to be'), [])

    def test_all_long(self): self.assertEqual(long_words(1, 'hello world yes'), ['hello', 'world', 'yes'])

    def test_with_punctuation(self): self.assertEqual(long_words(3, 'hello, world! fine.'), ['hello,', 'world!', 'fine.'])

    def test_multiple_spaces(self): self.assertEqual(long_words(2, 'a  big   fox'), ['big', 'fox'])

    def test_empty_string(self): self.assertEqual(long_words(3, ''), [])

    def test_numeric_words(self): self.assertEqual(long_words(2, '1234 56 7'), ['1234', '56'])

    def test_zero_threshold(self): self.assertEqual(long_words(0, 'hi to be'), ['hi', 'to', 'be'])

    def test_negative_threshold(self): self.assertEqual(long_words(-1, 'x y z'), ['x', 'y', 'z'])

    def test_newlines_tabs(self): self.assertEqual(long_words(2, 'a\nb c\tde'), ['a\nb', 'c\tde'])

