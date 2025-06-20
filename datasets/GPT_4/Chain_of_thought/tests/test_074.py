import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_074 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tup_string(('hello', 'world')), 'helloworld')

    def test_empty_tuple(self):
        self.assertEqual(tup_string(()), '')

    def test_single_element(self):
        self.assertEqual(tup_string(('single',)), 'single')

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            tup_string((1, 2, 3))

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            tup_string(('hello', 2, 3.5))

    def test_special_characters(self):
        self.assertEqual(tup_string(('#', '@', '$')), '#@$')

    def test_tuple_with_spaces(self):
        self.assertEqual(tup_string(('hello ', 'world')), 'hello world')

    def test_large_strings(self):
        large_string = 'a' * 10000
        self.assertEqual(tup_string((large_string, large_string)), large_string * 2)

    def test_repeated_elements(self):
        self.assertEqual(tup_string(('repeat', 'repeat', 'repeat')), 'repeatrepeatrepeat')

    def test_none_value(self):
        with self.assertRaises(TypeError):
            tup_string(('hello', None, 'world'))

