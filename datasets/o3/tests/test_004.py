import unittest
from datasets.o3.programs.program_004 import *

class TestVersion(unittest.TestCase):
    def test_simple_camel(self):
        self.assertEqual(text_lowercase_underscore("CamelCase"), "camel_case")

    def test_already_snake(self):
        self.assertEqual(text_lowercase_underscore("already_snake"), "already_snake")

    def test_acronym_handling(self):
        self.assertEqual(text_lowercase_underscore("HTTPServerError"), "http_server_error")

    def test_mixed_digits(self):
        self.assertEqual(text_lowercase_underscore("Version2Point0"), "version2_point0")

    def test_empty_string(self):
        self.assertEqual(text_lowercase_underscore(""), "")

    def test_single_lowercase(self):
        self.assertEqual(text_lowercase_underscore("lowercase"), "lowercase")

    def test_single_uppercase(self):
        self.assertEqual(text_lowercase_underscore("X"), "x")

