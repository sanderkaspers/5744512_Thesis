import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_050 import *

class TestVersion(unittest.TestCase):
    def test_standard_case(self): self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')

    def test_single_word(self): self.assertEqual(snake_to_camel('word'), 'Word')

    def test_multiple_underscores(self): self.assertEqual(snake_to_camel('one_two_three_four'), 'OneTwoThreeFour')

    def test_trailing_underscore(self): self.assertEqual(snake_to_camel('test_'), 'Test')

    def test_leading_underscore(self): self.assertEqual(snake_to_camel('_test'), 'Test')

    def test_double_underscores(self): self.assertEqual(snake_to_camel('hello__world'), 'HelloWorld')

    def test_all_lowercase(self): self.assertEqual(snake_to_camel('a_b_c'), 'ABC')

    def test_all_uppercase(self): self.assertEqual(snake_to_camel('A_B_C'), 'ABC')

    def test_mixed_case(self): self.assertEqual(snake_to_camel('snake_Case_to_Camel'), 'SnakeCaseToCamel')

    def test_empty_string(self): self.assertEqual(snake_to_camel(''), '')

