import unittest
from datasets.o3.programs.program_070 import *

class TestVersion(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(long_words(4, "hello world program"), ["hello", "world", "program"])

    def test_threshold_exclusive(self):
        self.assertEqual(long_words(5, "hello world program"), ["program"])

    def test_all_short(self):
        self.assertEqual(long_words(10, "a bb ccc"), [])

    def test_empty_string(self):
        self.assertEqual(long_words(3, ""), [])

    def test_mixed_length(self):
        text = "openai creates powerful models"
        self.assertEqual(long_words(6, text), ["creates", "powerful", "models"])

