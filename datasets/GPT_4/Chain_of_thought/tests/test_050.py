import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_050 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(snake_to_camel('this_is_a_test'), 'ThisIsATest')

    def test_single_word(self):
        self.assertEqual(snake_to_camel('hello'), 'Hello')

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_leading_trailing_underscores(self):
        self.assertEqual(snake_to_camel('_leading_and_trailing_'), 'LeadingAndTrailing')

    def test_consecutive_underscores(self):
        self.assertEqual(snake_to_camel('this__is__a__test'), 'ThisIsATest')

    def test_all_uppercase(self):
        self.assertEqual(snake_to_camel('THIS_IS_UPPERCASE'), 'ThisIsUppercase')

    def test_all_lowercase(self):
        self.assertEqual(snake_to_camel('this_is_lowercase'), 'ThisIsLowercase')

    def test_string_with_numbers(self):
        self.assertEqual(snake_to_camel('this_is_4_you'), 'ThisIs4You')

    def test_string_with_special_characters(self):
        self.assertEqual(snake_to_camel('this_is_a_test!'), 'ThisIsATest!')

    def test_mixed_case(self):
        self.assertEqual(snake_to_camel('this_IS_Mixed_Case'), 'ThisIsMixedCase')

