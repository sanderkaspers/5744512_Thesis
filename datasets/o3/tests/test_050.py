import unittest
from datasets.o3.programs.program_050 import *

class TestVersion(unittest.TestCase):
    def test_snake_basic(self):
        self.assertEqual(snake_to_camel("hello_world"), "HelloWorld")

    def test_single_word(self):
        self.assertEqual(snake_to_camel("python"), "Python")

    def test_multiple_underscores(self):
        self.assertEqual(snake_to_camel("hello__world"), "HelloWorld")

    def test_leading_underscore(self):
        self.assertEqual(snake_to_camel("_leading"), "Leading")

    def test_trailing_underscore(self):
        self.assertEqual(snake_to_camel("trailing_"), "Trailing")

    def test_all_caps(self):
        self.assertEqual(snake_to_camel("HELLO_WORLD"), "HelloWorld")

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(""), "")

