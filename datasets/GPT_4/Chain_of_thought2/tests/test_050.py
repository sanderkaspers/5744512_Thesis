import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_050 import *

class TestVersion(unittest.TestCase):
    def test_basic_two_words(self): self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')

    def test_multiple_words(self): self.assertEqual(snake_to_camel('get_http_response'), 'GetHttpResponse')

    def test_single_word_lowercase(self): self.assertEqual(snake_to_camel('word'), 'Word')

    def test_already_camel_case_input(self): self.assertEqual(snake_to_camel('AlreadyCamel'), 'Alreadycamel')

    def test_leading_underscore(self): self.assertEqual(snake_to_camel('_start'), '_Start')

    def test_trailing_underscore(self): self.assertEqual(snake_to_camel('end_'), 'End_')

    def test_consecutive_underscores(self): self.assertEqual(snake_to_camel('a__b'), 'A_B')

    def test_empty_string(self): self.assertEqual(snake_to_camel(''), '')

    def test_only_underscores(self): self.assertEqual(snake_to_camel('___'), '___')

    def test_mixed_case_input(self): self.assertEqual(snake_to_camel('snake_Case_Input'), 'SnakeCaseInput')

