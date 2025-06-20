import unittest
from datasets.GPT_4.Few_shot2.programs.program_004 import *

class TestVersion(unittest.TestCase):
    def test_text_lowercase_underscore_camel_case(self): self.assertEqual(text_lowercase_underscore('camelCase'), 'camel_case')

    def test_text_lowercase_underscore_pascal_case(self): self.assertEqual(text_lowercase_underscore('PascalCase'), '_pascal_case')

    def test_text_lowercase_underscore_all_upper(self): self.assertEqual(text_lowercase_underscore('ABC'), '_a_b_c')

    def test_text_lowercase_underscore_single_upper_start(self): self.assertEqual(text_lowercase_underscore('Hello'), '_hello')

    def test_text_lowercase_underscore_single_upper_mid(self): self.assertEqual(text_lowercase_underscore('helloWorld'), 'hello_world')

    def test_text_lowercase_underscore_no_uppercase(self): self.assertEqual(text_lowercase_underscore('already_lower'), 'already_lower')

    def test_text_lowercase_underscore_empty_string(self): self.assertEqual(text_lowercase_underscore(''), '')

    def test_text_lowercase_underscore_numbers_and_caps(self): self.assertEqual(text_lowercase_underscore('A1B2C3'), '_a1_b2_c3')

    def test_text_lowercase_underscore_with_underscores(self): self.assertEqual(text_lowercase_underscore('With_Underscores'), '_with__underscores')

    def test_text_lowercase_underscore_special_characters(self): self.assertEqual(text_lowercase_underscore('HelloWorld!'), '_hello_world!')

