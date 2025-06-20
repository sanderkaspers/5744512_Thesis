import unittest
from datasets.GPT_4.Few_shot2.programs.program_050 import *

class TestVersion(unittest.TestCase):
    def test_snake_to_camel_basic(self): self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')

    def test_snake_to_camel_single_word(self): self.assertEqual(snake_to_camel('hello'), 'Hello')

    def test_snake_to_camel_leading_underscore(self): self.assertEqual(snake_to_camel('_start'), 'Start')

    def test_snake_to_camel_trailing_underscore(self): self.assertEqual(snake_to_camel('end_'), 'End')

    def test_snake_to_camel_multiple_underscores(self): self.assertEqual(snake_to_camel('this__is__test'), 'ThisIsTest')

    def test_snake_to_camel_empty_string(self): self.assertEqual(snake_to_camel(''), '')

    def test_snake_to_camel_all_underscores(self): self.assertEqual(snake_to_camel('___'), '')

    def test_snake_to_camel_numbers_in_word(self): self.assertEqual(snake_to_camel('section_2_part_3'), 'Section2Part3')

    def test_snake_to_camel_already_camel(self): self.assertEqual(snake_to_camel('CamelCase'), 'Camelcase')

    def test_snake_to_camel_mixed_case(self): self.assertEqual(snake_to_camel('snake_Case_test'), 'SnakeCaseTest')

